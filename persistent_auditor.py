def load_inventory():
    try:
        file = open("inventory.txt", 'r')

        total_units = int(file.readline())

        history_data = file.readline().split(",")
        transaction_history = []

        for amount in history_data:
            if amount != "":
                transaction_history.append(int(amount))

        file.close()

        return total_units, transaction_history

    except FileNotFoundError:
        return 0, []


inventory, transaction_history = load_inventory()
failed_entries = 0


def get_valid_input():

    stock = input("Enter stock quantity (or type 'quit' to stop): ")

    if stock.lower() == 'quit':
        return "quit", False

    if not stock.isdigit():
        print("Please enter a valid integer")
        return None, True

    stock = int(stock)

    if stock < 0:
        print("Negative numbers are not allowed")
        return None, True

    return stock, False


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.1
    return tax


def generate_report(total_units, failed_attempts):
    print("Total deliveries processed:", total_units)
    print("Number of fialed/ rejected entries:", failed_attempts)


while True:
    value, failed = get_valid_input()

    if failed:
        failed_entries += 1
        continue

    if value == "quit":
        break

    inventory = process_delivery(inventory, value)
    transaction_history.append(value)
    tax = calculate_tax(value)



def save_inventory(total_units, transaction_history):
    file = open("inventory.txt", "w")
    file.write(str(total_units) + "\n")

    for amount in transaction_history:
        file.write(str(amount) + ",")

    file.close()

save_inventory(inventory, transaction_history)
generate_report(inventory, failed_entries)
