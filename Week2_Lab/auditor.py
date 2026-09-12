inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or type 'quite' to stop): ")

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

    
    inventory += stock

    if inventory > 500:
         print("Inventory exceeds 500 units")
         break