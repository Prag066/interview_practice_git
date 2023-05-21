import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    with open(csv_file_path, 'r') as csv_file:
        # Assuming the CSV file has a header row
        csv_reader = csv.DictReader(csv_file)
        # Convert each row into a dictionary and collect them in a list
        data = [row for row in csv_reader]

    # Write the JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Specify the path to the CSV file and the desired JSON file
csv_file_path = '/Users/hacker/Developer/patterns/a.csv'
json_file_path = '/Users/hacker/Developer/patterns/output.json'

# Convert the CSV file to JSON
csv_to_json(csv_file_path, json_file_path)
