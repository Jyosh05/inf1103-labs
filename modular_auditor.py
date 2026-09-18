inventory = 0
failed_entries = 0


def get_valid_input():

    stock = input("Enter stock quantity (or type 'quit' to stop): ")

    if stock.lower() == 'quit':
        return "quit"

    if not stock.isdigit():
        print("Please enter a valid integer")
        return None

    stock = int(stock)

    if stock < 0:
        print("Negative numbers are not allowed")
        return None

    return stock







get_valid_input()
