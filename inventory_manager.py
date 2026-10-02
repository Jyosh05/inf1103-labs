# Step 1: Create the initial inventory list with 3 dictionaries
# Step 2: Create display_all()
# Step 3: Create add_product()
# Step 4: Create update_stock()
# Step 5: Create search_product()
# Step 6: Create load_inventory() and save_inventory() using JSON
# Step 7: Put everything into the menu

import json

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

def display_all(inventory):
    for inv in inventory:
        print(f"ID: {inv['id']} | Name: {inv['name']} | Price: ${inv['price']} | Stock: {inv['stock']}")


def add_product(inventory):
    productID = input("Product ID: ")
    productName = input("Product Name: ")
    Price = float(input("Price: "))
    stockQuantity = int(input("Stock Quantity: "))

    new_inv = dict(id=productID, name=productName, price=Price, stock=stockQuantity)
    inventory.append(new_inv)

    print("Product added successfully!")


def update_stock(inventory):
    Id = input("Enter Product ID: ")

    for inv in inventory:
        if inv['id'] == Id:
            print("Product Found:")
            print(f"Name: {inv['name']}")
            print(f"Current Stock: {inv['stock']}")

            stockQuantity = int(input("New Stock Quantity: "))
            inv['stock'] = stockQuantity

            print("Stock updated successfully!")
            break

    else:
            print("Product not found")
            
        
def search_product(inventory):
    print("Search Product")
    Id = input("Enter Product ID: ")
     
    for inv in inventory:
        if inv['id'] == Id:
            print("Product Found:")
            print("------------------------------------------------")
            print(f"ID: {inv['id']}")
            print(f"Name: {inv['name']}")
            print(f"Price: ${inv['price']}")
            print(f"Stock: {inv['stock']}")
            print("------------------------------------------------")

            break
     
    else:
        print("Product not found")


def load_inventory():
    try:
        with open('inventory.json',  'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open('inventory.json', 'w', encoding='utf-8') as file:
        json.dump(inventory, file)
        



print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = load_inventory()

if inventory:
    print("inventory.json found")
    print("Inventory loaded successfully")

print("----------- MENU -----------")
print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Exit")
print("----------------------------")

while True:
    user_input = input("Enter option: ")

    if user_input == '1':
        display_all(inventory)

    elif user_input == '2':
        add_product(inventory)

    elif user_input == '3':
        update_stock(inventory)

    elif user_input == '4':
        search_product(inventory)

    elif user_input == '5':
        save_inventory(inventory)
        print("Saving inventory before exit...")
        print("Inventory saved successfully to inventory.json")

    elif user_input == '6':
        save_inventory(inventory)
        print("Saving inventory before exit...")
        print("Inventory saved successfully")

        print("Thank you for using Inventory Management System")
        print("Program terminated")
        break

    else:
        print("Invalid input entered. Please enter the correct input")
