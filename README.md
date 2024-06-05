# ServiceTitanInternship
 This project processes invoice data from a pickle file, transforms it into a structured CSV format, and checks for expired invoices.

## Data Extraction and Transformation (transform_data.py)
### Class Initialization:
Initializes with paths to the invoice data and expired invoice IDs.
Sets up a type mapping dictionary for converting item types.

### Data Loading:
Loads the invoice data from invoices_new.pkl.
Loads expired invoice IDs from expired_invoices.txt and stores them

### Data Transformation:
Normalizes invoice IDs by removing non-numeric characters.
Safely converts unit prices and quantities to integers, with specific handling for string representations of numbers.
Maps item types to predefined categories.
Calculates total price and percentage of the total invoice for each item.
Marks invoices as expired based on the loaded IDs.

### Saving Data:
Transforms the data into a pandas DataFrame.
Sorts the DataFrame by invoice_id and invoiceitem_id.
Saves the DataFrame to invoices_transformed.csv.
Expired Invoices Validation (check.py)

### Loading Data:
Loads the transformed DataFrame from invoices_transformed.csv.
Loads the set of expired invoice IDs from expired_invoices.txt.

### Validation:
Checks if the is_expired field in the DataFrame matches the expected expired status.
Prints the number of correctly identified expired items.
Returns a DataFrame of incorrectly identified items for further inspection.

## Files
check.py: I wrote a script to verify the correctness of invoice data. It reads in invoice data from a file, checks for any anomalies or inconsistencies and outputs a report detailing any issues found, providing insights into the quality and integrity of my code.

non_integer.py: checks strings in Quantity that are integers