import csv

def read_csv_to_dict_of_dicts(file_path):
    result_dict = {}
    
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Assuming the first row contains headers
        headers = next(csv_reader)
        
        for row in csv_reader:
            # Use the value in the first column as the key
            key = row[0]
            
            # Create a dictionary for the current row using the headers as keys
            row_dict = {headers[i]: row[i] for i in range(1, len(headers))}
            
            # Add the row dictionary to the result dictionary using the key
            result_dict[key] = row_dict

    return result_dict

# Provide the path to your CSV file
file_path = 'csv1.csv'

# Call the function to read the CSV file and create the dictionary of dictionaries
result = read_csv_to_dict_of_dicts(file_path)

# Print the result
print(result)
