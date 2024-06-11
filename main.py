import csv
import json
from datetime import datetime

# Specify the input CSV file name
input_csv_file = 'TCS.NS.csv'
# Specify the output JSON file name
output_json_file = 'data.json'

# Read the CSV file
data = []
with open(input_csv_file, newline='') as csvfile:
    isSkipHeader=False
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Logic for skipping the Header
        if(isSkipHeader is False):
            isSkipHeader = True
            continue

        # Add all the columns apart from first i.e. Date
        currentRow = [float(val) for val in row[1:5]]
        # Parse date to Unix time format (ms)
        currentRow.insert(0,datetime.strptime(row[0], "%d-%m-%Y").timestamp() * 1000)
        # Append to the overall data
        data.append(currentRow)  

# Write the data to a JSON file in the desired format
with open(output_json_file, 'w') as jsonfile:
    json.dump(data, jsonfile)

print("Data successfully converted to JSON format and saved to", output_json_file)