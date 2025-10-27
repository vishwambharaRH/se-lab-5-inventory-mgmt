import json
# import logging  # Pylint W0611/Flake8 F401: Removed unused import
from datetime import datetime

# Global variable
stock_data = {}


# Flake8 E302: Added 2 blank lines
def add_item(item="default", qty=0, logs=None):  # Pylint W0102: Fixed dangerous default value []
    if logs is None:
        logs = []

    # Added type checking to fix bug from main()
    if not isinstance(qty, int):
        print(f"Error: Quantity '{qty}' for item '{item}' is not an integer. Skipping.")
        return

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    # Pylint C0209: Converted to f-string
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # Bandit B110/Pylint W0702/Flake8 E722: Replaced bare 'except' with specific 'KeyError'
    except KeyError:
        # This silently fails if the item doesn't exist, which was the original intent of 'pass'
        pass


def get_qty(item):
    # Fixed potential KeyError bug from original code
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    global stock_data  # Pylint W0603: Global is necessary for this design
    try:
        # Pylint R1732: Use 'with' for file operations
        # Pylint W1514: Added 'encoding'
        with open(file, "r", encoding="utf-8") as f:
            data = f.read()
            if data:
                stock_data = json.loads(data)
            else:
                stock_data = {}  # Handle empty file
    except FileNotFoundError:
        print(f"Info: {file} not found. Starting with empty inventory.")
        stock_data = {}
    except json.decoder.JSONDecodeError:
        print(f"Warning: {file} is corrupt. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    try:
        # Pylint R1732: Use 'with' for file operations
        # Pylint W1514: Added 'encoding'
        with open(file, "w", encoding="utf-8") as f:
            # Added indent=4 for human-readable JSON
            f.write(json.dumps(stock_data, indent=4))
    except IOError as e:
        print(f"Error: Could not save data to {file}. {e}")


def print_data():
    print("Items Report")
    for i in stock_data:
        # Converted to f-string for consistency
        print(f"{i} -> {stock_data[i]}")


def check_low_items(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    # Load data at the start to persist inventory
    load_data()
    
    # Initialize log list correctly
    my_logs = []

    add_item("apple", 10, my_logs)
    add_item("banana", -2, my_logs)
    add_item(123, "ten", my_logs)  # Now safely handled by type check
    remove_item("apple", 3)
    remove_item("orange", 1)  # Now safely handled by 'except KeyError'

    print("Apple stock:", get_qty("apple"))
    print("Orange stock:", get_qty("orange"))  # Now safely handled by .get()
    print("Low items:", check_low_items())

    print_data()
    # Save data at the end
    save_data()

    # Bandit B307/Pylint W0123: Removed dangerous eval()
    print('eval used')
    
    # print("\n--- Logs ---")
    # for log in my_logs:
    #     print(log)


main()
# Pylint C0304/Flake8 W292: Added final newline