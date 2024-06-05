import pickle

# Load the pickle file
with open('invoices_new.pkl', 'rb') as file:
    invoices_data = pickle.load(file)

# Collect all non-integer quantities
non_integer_quantities = []

# Loop over each invoice and its details
for invoice in invoices_data:
    if 'items' in invoice:
        for item in invoice['items']:
            quantity = item['quantity']
            try:
                # Attempt to convert the quantity to an integer
                _ = int(quantity)
            except ValueError:
                # If it fails, this means the quantity is not an integer
                non_integer_quantities.append((invoice['id'], item['item']['id'], quantity))

# Print out non-integer quantities
for invoice_id, item_id, quantity in non_integer_quantities:
    print(f"Invoice ID: {invoice_id}, Item ID: {item_id}, Non-integer Quantity: '{quantity}'")
