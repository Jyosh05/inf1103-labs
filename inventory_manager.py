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
        print(f"ID: {inv['id']} | Name: {inv['name']} | Price: {inv['price']} | Stock: {inv['stock']}")


def add_product(inventory):
    productID = input("Product ID: ")
    productName = input("Product Name: ")
    Price = float(input("Price: "))
    stockQuantity = int(input("Stock Quantity: "))

    new_inv = dict(id=productID, name=productName, price=Price, stock=stockQuantity)
    inventory.append(new_inv)


def update_stock(inventory):
    Id = input("Enter Product ID: ")

    for inv in inventory:
        if inv['id'] == Id:
            print("Product Found:")
            print(f"Name: {inv.name}")
            print(f"Current Stock: {inv.stock}")

            stockQuantity = int(input("New Stock Quantity: "))
            inv['stock'] = stockQuantity

            print("Stock updated successfully!")
            break

    else:
            print("Product not found")
            
        
def search_product(inventory):
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
            print("File found")
    except FileNotFoundError:
        return []

load_inventory()

# add_product(inventory)
# display_all(inventory)
# update_stock(inventory)
# search_product(inventory)
