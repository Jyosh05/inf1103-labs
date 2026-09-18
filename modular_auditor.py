inventory = 0
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
    new_value += current_total
    return new_value

def calculate_tax(amount):
    tax = amount * 0.1
    return tax


def generate_report(total_units, failed_attempts):
    print("Total units processed:", total_units)
    print("Number of fialed/ rejected entries:", failed_attempts)



get_valid_input()
