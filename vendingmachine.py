# List of items with item information including item ID, name, price, and initial stock
items_data = [
    {"itemId": 1, "itemName": "Pepsi", 'DHS': 2, 'stock': 10},
    {"itemId": 2, "itemName": "Coca-Cola", 'DHS': 2, 'stock': 10},
    {"itemId": 3, "itemName": "Sprite", 'DHS': 2, 'stock': 10},
    {"itemId": 4, "itemName": "Fanta", 'DHS': 2, 'stock': 10},
    {"itemId": 5, "itemName": "7up", 'DHS': 2, 'stock': 10},
    {"itemId": 6, "itemName": "Shani", 'DHS': 2, 'stock': 10},
    {"itemId": 7, "itemName": "Chocolate Milk", 'DHS': 1, 'stock': 10},
    {"itemId": 8, "itemName": "Strawberry Milk", 'DHS': 1, 'stock': 10},
    {"itemId": 9, "itemName": "Iced tea", 'DHS': 4, 'stock': 10},
    {"itemId": 10, "itemName": "Iced Coffee", 'DHS': 4, 'stock': 10},
    {"itemId": 11, "itemName": "RedBull", 'DHS': 6, 'stock': 10},
    {"itemId": 12, "itemName": "Lays", 'DHS': 1, 'stock': 10},
    {"itemId": 13, "itemName": "KitKat", 'DHS': 2, 'stock': 10},
    {"itemId": 14, "itemName": "Cookies", 'DHS': 5, 'stock': 10},
    {"itemId": 15, "itemName": "Pound Cake", 'DHS': 10, 'stock': 10},
    {"itemId": 16, "itemName": "Cheetos", 'DHS': 3, 'stock': 10},
    {"itemId": 17, "itemName": "Spearmint Gum", 'DHS': 1, 'stock': 10},
    {"itemId": 18, "itemName": "Swiss Roll", 'DHS': 2, 'stock': 10},
    {"itemId": 19, "itemName": "Snicker Bar", 'DHS': 2, 'stock': 10},
    {"itemId": 20, "itemName": "Twix", 'DHS': 2, 'stock': 10},
]

# Initialize variables for user selections, receipt, total amount, user money, and program run
item = []
receipt = """\n\t\tPRODUCT NAME -- COST\n"""
total_amount = 0
user_money = 0
run = True

# Display welcome message and initial list of items in stock
print("------- Aamir's Vending Machine -------\n\n")
print("---------- The Items In Stock Are ----------\n\n")


# Function to display items
def display_items():
    for i in items_data:
        print(f"Item: {i['itemName']} --- DHS: {i['DHS']} --- Stock: {i['stock']} --- Item ID: {i['itemId']}")


# Function to prompt the user to insert money
def get_user_money():
    global user_money
    while True:
        try:
            user_money = float(input("Insert money (DHS): "))
            if user_money < 0:
                print("Please enter a valid amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


# Function to update the inventory after a successful purchase
def update_inventory(item):
    for i in item:
        for j in items_data:
            if i["itemId"] == j["itemId"]:
                j['stock'] -= 1


# Function to categorize items into refreshments and snacks
def categorize_items():
    refreshments = items_data[:11]
    snacks = items_data[11:]
    return refreshments, snacks


# Main function to simulate the vending machine
def vendingMachine(items_data, run, item):
    global total_amount
    refreshments, snacks = categorize_items()

    while run:
        # Display Refreshments Menu
        print("\nRefreshments Menu:")
        for i in refreshments:
            print(f"Item: {i['itemName']} --- DHS: {i['DHS']} --- Stock: {i['stock']} --- Item ID: {i['itemId']}")
        # Display Snacks Menu
        print("\nSnacks Menu:")
        for i in snacks:
            print(f"Item: {i['itemName']} --- DHS: {i['DHS']} --- Stock: {i['stock']} --- Item ID: {i['itemId']}")

        # Prompt the user to enter the item code for the desired item
        buyItem = int(input("\n\nEnter the item code for the item you want to buy: "))

        # Validate the item code and stock availability
        if 0 <= buyItem < len(items_data) and items_data[buyItem]['stock'] > 0:
            item.append(items_data[buyItem])
            total_amount += items_data[buyItem]["DHS"]
        else:
            print("Invalid item code or out of stock!")

        # Prompt the user for further actions (add more items, purchase, or stop)
        moreItems = input("Input any key to add more items, 'p' to purchase, and 'q' to stop: ")
        if moreItems.lower() == "q":
            run = False
        elif moreItems.lower() == "p":
            get_user_money()
            if user_money < total_amount:
                print("Insufficient funds. Please add more money.")
            else:
                update_inventory(item)
                print("Transaction successful!")
                break


# Function to calculate the total cost of items in the user's basket
def sumItem(item):
    sumItems = 0
    for i in item:
        sumItems += i["DHS"]
    return sumItems


# Function to create a receipt for the user
def createReceipt(item, receipt):
    for i in item:
        receipt += f"\t{i['itemName']} -- {i['DHS']} DHS\n"
    receipt += f"\tTotal --- {sumItem(item)} DHS\n"
    return receipt


# Main Code
vendingMachine(items_data, run, item)
print(createReceipt(item, receipt))