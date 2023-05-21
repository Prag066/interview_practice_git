import pandas as pd
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file using pandas
    data = pd.read_csv(csv_file_path)

    # Convert the data to JSON format
    json_data = data.to_json(orient='records')

    # Write the JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

# Specify the path to the CSV file and the desired JSON file
csv_file_path = '/Users/hacker/Developer/patterns/a.csv'
json_file_path = '/Users/hacker/Developer/patterns/output.json'

# Convert the CSV file to JSON
csv_to_json(csv_file_path, json_file_path)
