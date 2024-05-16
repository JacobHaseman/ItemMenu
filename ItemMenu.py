class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        print("Menu:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.name}: ${item.price}")

def main():
    # Create menu items
    burger = MenuItem("Burger", 5.99)
    fries = MenuItem("Fries", 2.49)
    chicken_tenders = MenuItem("Chicken Tenders", 6.99)
    chicken_sandwich = MenuItem("Chicken Sandwich", 5.99)
    soda = MenuItem("Soda", 1.99)

    # Create menu
    menu = Menu()
    menu.add_item(burger)
    menu.add_item(fries)
    menu.add_item(chicken_tenders)
    menu.add_item(chicken_sandwich)
    menu.add_item(soda)

    # Display menu
    menu.display()

    # Take order
    order = {}
    while True:
        choice = input("Enter the number of the item you'd like to order (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if choice < 1 or choice > len(menu.items):
                print("Invalid choice. Please enter a number between 1 and", len(menu.items))
                continue
            quantity = int(input("Enter the quantity: "))
            if quantity < 1:
                print("Quantity must be at least 1.")
                continue
            item = menu.items[choice - 1]
            if item.name in order:
                order[item.name] += quantity
            else:
                order[item.name] = quantity
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Print receipt
    print("\nReceipt:")
    total = 0
    for item, quantity in order.items():
        price = menu.items[[menu_item.name for menu_item in menu.items].index(item)].price
        item_total = price * quantity
        total += item_total
        print(f"{item}: ${price} x {quantity} = ${item_total}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
