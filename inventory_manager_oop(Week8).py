import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price}, Stock: {self.__stock}")


#helper functions (getters) so other funtions can access private data
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name
        
    def get_stock(self):
        return self.__stock

    #helper method to convert the object back to a dictionary for saving to JSON
    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name, "price": self.__price, "stock": self.__stock}

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products: 
                product.display_information()

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
            return None

    #helper to get the list of products for saving
    def get_all_products(self):
        return self.__products


def load_inventory():
    inv_system = Inventory()
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            for item in data:
                product = Product(item['id'], item['name'], item['price'], item['stock'])
                inv_system.add_product(product)

            print("inventory.json found")
            print("Inventory loaded successfully")
    except FileNotFoundError:
        pass
    
    return inv_system

def save_inventory(inv_system):
    # Convert Product objects back to dictionaries for JSON
    dict_list = [product.to_dict() for product in inv_system.get_all_products()]
    with open('inventory.json', 'w', encoding='utf-8') as file:
        json.dump(dict_list, file, indent=4)


# --- 3. MAIN PROGRAM ---

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

# Initialize inventory system by loading from file
my_inventory = load_inventory()

while True:
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    
    user_input = input("Enter option: ")

    if user_input == '1':
        my_inventory.display_all()

    elif user_input == '2':
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        
        # Create a new Product object and pass it to Inventory
        new_product = Product(product_id, name, price, stock)
        my_inventory.add_product(new_product)
        print("Product added successfully!")

    elif user_input == '3':
        product_id = input("Enter Product ID: ")
        # Ask inventory to find the object
        found_product = my_inventory.search_product(product_id)
        
        if found_product:
            print("Product Found:")
            print(f"Name: {found_product.get_name()}")
            print(f"Current Stock: {found_product.get_stock()}")
            
            new_stock = int(input("New Stock Quantity: "))
            # Call the product's own method to update its state
            found_product.update_stock(new_stock)
            print("Stock updated successfully!")
        else:
            print("Product not found")

    elif user_input == '4':
        print("Search Product")
        product_id = input("Enter Product ID: ")
        found_product = my_inventory.search_product(product_id)
        
        if found_product:
            print("Product Found:")
            print("------------------------------------------------")
            found_product.display_information()
            print("------------------------------------------------")
        else:
            print("Product not found")

    elif user_input == '5':
        save_inventory(my_inventory)
        print("Inventory saved successfully to inventory.json")

    elif user_input == '6':
        print("Saving inventory before exit...")
        save_inventory(my_inventory)
        print("Inventory saved successfully")
        print("Thank you for using Inventory Management System")
        print("Program terminated")
        break

    else:
        print("Invalid input entered. Please enter the correct input")