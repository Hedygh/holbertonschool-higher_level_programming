#!/usr/bin/python3
"""read from CSV and convert to JSON"""

import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file to JSON file"""
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w") as out:
            json.dump(data, out, indent=4)
        return True
    except FileNotFoundError:
        return False
