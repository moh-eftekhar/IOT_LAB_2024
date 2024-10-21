import json
import datetime as dt

# Read the data from the file
def load_data():
    try:
        with open("catalog.json", "r") as file:
            data = json.load(file)
            print("Data loaded successfully!")
            return data
    except FileNotFoundError:
        data = []

print(load_data())