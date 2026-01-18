from Data import Data
import json
import os

def load_data(filename):
    if not os.path.exists(filename):
        print("No data file found. Starting with empty data.")
        return Data(1000, {}, [])

    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
            return Data(
                data.get("balance", 1000),
                data.get("warehouse", {}),
                data.get("operations", [])
            )

    except (IOError, json.JSONDecodeError):
        print("Error reading data file. Starting fresh.")
        return Data(1000, {}, [])



