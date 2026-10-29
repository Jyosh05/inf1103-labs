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

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def display_all(self):
        for product in self.__products():
            product.display_information()

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
            return None