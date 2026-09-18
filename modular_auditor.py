inventory = 0
failed_entries = 0

# while True:
#     stock = input("Enter stock quantity (or type 'quit' to stop): ")

#     if stock.lower() == 'quit':
#         break

#     if not stock.isdigit():
#             print("Please enter a valid integer")
#             failed_entries +=1
#             continue
    
#     stock = int(stock)
   
#     if stock < 0:
#         print("Negative numbers are not allowed")
#         failed_entries += 1
#         continue

    
#     inventory += stock

#     if inventory > 500:
#          print("Inventory exceeds 500 units")
#          break


# print("Total Units Processed: ", inventory)
# print("Number of failed/ rejected entries: ", failed_entries)
    

def get_valid_input(inventory, failed_entries):

    while True:

        stock = input("Enter stock quantity (or type 'quit' to stop): ")

        if stock.lower() == 'quit':
            break

        if not stock.isdigit():
            print("Please enter a valid integer")
            failed_entries +=1
            continue

        stock = int(stock)

        if stock < 0:
            print("Negative numbers are not allowed")
            failed_entries += 1
            continue

    return stock, failed_entries

get_valid_input(inventory, failed_entries)

