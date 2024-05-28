#!/usr/bin/env python3
"""Python Module to gain experience in reading data \
from one format (CSV) and converting it into another \
format (JSON) using serialization techniques."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Function to convert a CSV file to a JSON file."""
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        json_data = json.dumps(data)

        with open('data.json', 'w') as json_file:
            json_file.write(json_data)
        return True
    except FileNotFoundError:
        print("Error: File not found.")
        return False
