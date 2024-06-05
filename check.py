import pandas as pd

def check_expired_items(invoices_csv_path, expired_ids_path):
    # Load the transformed DataFrame
    df = pd.read_csv(invoices_csv_path)

    # Load the set of expired invoice IDs
    with open(expired_ids_path, 'r') as file:
        expired_invoices = set(file.read().strip().split(', '))

    # Normalize the IDs if necessary (e.g., removing non-digit characters)
    expired_invoices = {invoice.strip() for invoice in expired_invoices}

    # Check the 'is_expired' flag accuracy
    df['correctly_identified'] = df['invoice_id'].apply(lambda x: str(x) in expired_invoices) == df['is_expired']

    # Report the results
    correct_identifications = df['correctly_identified'].sum()
    total_checks = len(df)
    print(f"Correctly identified expired items: {correct_identifications} out of {total_checks} checks.")

    # Optionally, return or examine rows that were incorrectly identified
    incorrect_identifications = df[~df['correctly_identified']]
    return incorrect_identifications

# Usage
incorrect_items = check_expired_items('invoices_transformed.csv', 'expired_invoices.txt')
print("Incorrectly identified items:")
print(incorrect_items)

