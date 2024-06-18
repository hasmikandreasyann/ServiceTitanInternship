import pickle

# Load the pickle file
with open('invoices_new.pkl', 'rb') as file:
    invoices_data = pickle.load(file)
#
# # Print each invoice and its details
# for invoice in invoices_data:
#     print(f"Invoice ID: {invoice['id']}")
#     print(f"Created On: {invoice['created_on']}")
#     if 'items' in invoice:
#         for item in invoice['items']:
#             print(f"  Item ID: {item['item']['id']}")
#             print(f"  Item Name: {item['item']['name']}")
#             print(f"  Unit Price: {item['item']['unit_price']}")
#             print(f"  Type: {item['item']['type']}")
#             print(f"  Quantity: {item['quantity']}")
#     print("\n")

# Generate the text content from the given data
content = []

# Loop over each invoice and its details
for invoice in invoices_data:
    invoice_details = f"Invoice ID: {invoice['id']}\n"
    invoice_details += f"Created On: {invoice['created_on']}\n"
    if 'items' in invoice:
        for item in invoice['items']:
            invoice_details += f"  Item ID: {item['item']['id']}\n"
            invoice_details += f"  Item Name: {item['item']['name']}\n"
            invoice_details += f"  Unit Price: {item['item']['unit_price']}\n"
            invoice_details += f"  Type: {item['item']['type']}\n"
            invoice_details += f"  Quantity: {item['quantity']}\n"
    invoice_details += "\n"
    content.append(invoice_details)

# Join all content into a single string
output_text = "\n".join(content)

# Save to a text file
with open("invoices_details.txt", "w") as text_file:
    text_file.write(output_text)

"invoices_details.txt"  # Return the path to the saved file
