import pandas as pd


class DataExtractor:
    def __init__(self, invoices_path, expired_invoices_path):
        self.invoices_path = invoices_path
        self.expired_invoices_path = expired_invoices_path
        self.type_mapping = {0: 'Material', 1: 'Equipment', 2: 'Service', 3: 'Other'}

    def safe_int_conversion(self, value):
        try:
            return int(value)
        except ValueError:
            number_mapping = {'five': 5, 'ten': 10}  
            return number_mapping.get(str(value).lower(), 0)

    def safe_type_mapping(self, item_type):
        # Convert item_type to int safely and map, default to 'Other' if unexpected
        try:
            item_type = int(item_type)
            return self.type_mapping.get(item_type, 'Other')
        except ValueError:
            return 'Other'

    def normalize_id(self, id_value):
        # Normalize IDs by removing any non-numeric characters
        return ''.join(filter(str.isdigit, str(id_value)))

    def load_data(self):
        # Load invoices data
        self.invoices_data = pd.read_pickle(self.invoices_path)

        # Load expired invoices and create a set for quick lookup
        with open(self.expired_invoices_path, 'r') as file:
            self.expired_invoices = set(self.normalize_id(id_str) for id_str in file.read().split(', '))

    def transform_data(self):
        data = []
        for invoice in self.invoices_data:
            if 'items' not in invoice:
                continue  # Skip invoices that do not contain any items
            invoice_id = self.normalize_id(invoice['id'])
            created_on = pd.to_datetime(invoice['created_on'], errors='coerce')  # Handle invalid dates ex` feb 30
            invoice_total = sum(
                self.safe_int_conversion(item['item']['unit_price']) * self.safe_int_conversion(item['quantity']) for
                item in invoice.get('items', []))
            is_expired = invoice_id in self.expired_invoices

            for item in invoice.get('items', []):
                item_id = item['item']['id']
                item_name = item['item']['name']
                unit_price = self.safe_int_conversion(item['item']['unit_price'])
                item_type = self.safe_type_mapping(item['item']['type'])
                quantity = self.safe_int_conversion(item['quantity'])
                total_price = unit_price * quantity
                percentage_in_invoice = total_price / invoice_total if invoice_total else 0

                data.append({
                    'invoice_id': invoice_id,
                    'created_on': created_on,
                    'invoiceitem_id': item_id,
                    'invoiceitem_name': item_name,
                    'type': item_type,
                    'unit_price': unit_price,
                    'total_price': total_price,
                    'percentage_in_invoice': percentage_in_invoice,
                    'is_expired': is_expired
                })

        self.df = pd.DataFrame(data)
        self.df.sort_values(by=['invoice_id', 'invoiceitem_id'], inplace=True)

    def save_to_csv(self, output_path):
        self.df.to_csv(output_path, index=False)


# Usage
extractor = DataExtractor('invoices_new.pkl', 'expired_invoices.txt')
extractor.load_data()
extractor.transform_data()
extractor.save_to_csv('invoices_transformed.csv')
