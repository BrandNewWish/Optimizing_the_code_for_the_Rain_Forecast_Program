import json


class Data:
    def __init__(self, balance=0, warehouse=None, operations=None):
        self.balance = balance
        self.warehouse = warehouse if warehouse is not None else {}
        self.operations = operations if operations is not None else []

    def save_to_file(self, filename):
        data = {
            "balance": self.balance,
            "warehouse": self.warehouse,
            "operations": self.operations
        }
        try:
            with open(filename, "w", encoding= "utf-8") as file:
                json.dump(data, file, indent=4)
        except IOError:
            print("Error saving data to file")


