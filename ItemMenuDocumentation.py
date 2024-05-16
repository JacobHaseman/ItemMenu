# This program is a documentation of the ItemMenu.py program.
# The program is a simple use of classes and objects to create a menu of items and their prices.
# The program creates two classes: MenuItem and Menu.

# MenuItem class has two attributes: name and price.

#class MenuItem:
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price


# Menu class has one attribute: items, which is a list of MenuItem objects.
# The Menu class has two methods: add_item and display.
# The add_item method appends a MenuItem object to the items list.
# The display method prints the menu items and their prices.

#class Menu:
#    def __init__(self):
#        self.items = []

#    def add_item(self, item):
#        self.items.append(item)

#    def display(self):
#        print("Menu:")
#        for index, item in enumerate(self.items, start=1):
#            print(f"{index}. {item.name}: ${item.price}")


# The main function which runs the program

#def main():


# This creates the menuItems using the MenuItem class.

    # Create menu items
#    burger = MenuItem("Burger", 5.99)
#    fries = MenuItem("Fries", 2.49)
#    chicken_tenders = MenuItem("Chicken Tenders", 6.99)
#    chicken_sandwich = MenuItem("Chicken Sandwich", 5.99)
#    soda = MenuItem("Soda", 1.99)


# This creates the menu using the Menu class.

    # Create menu
#    menu = Menu()
#    menu.add_item(burger)
#    menu.add_item(fries)
#    menu.add_item(chicken_tenders)
#    menu.add_item(chicken_sandwich)
#    menu.add_item(soda)


    # Displays the menu
#    menu.display()


# initialize an empty dictionary to store the order/orders

    # Take order
#    order = {}


# Will prompt the user to enter the number of item they'd like to order
# If the user enters 0, the loop will break and the program will proceed to print the receipt

#while True:
#        choice = input("Enter the number of the item you'd like to order (0 to finish): ")
#        if choice == '0':
#            break


# The program will try to convert the input to an integer
# If the input is not an integer, the program will print an error message and prompt the user to enter a number
# The program will check if the input is a valid choice
# The program will prompt the user to enter the quantity of the item they'd like to order
# The program will check if the quantity is at least 1
# The program will add the item to the order dictionary with the quantity as the value

#try:
#            choice = int(choice)
#            if choice < 1 or choice > len(menu.items):
#                print("Invalid choice. Please enter a number between 1 and", len(menu.items))
#                continue
#            quantity = int(input("Enter the quantity: "))
#            if quantity < 1:
#                print("Quantity must be at least 1.")
#                continue
#            item = menu.items[choice - 1]
#            if item.name in order:
#                order[item.name] += quantity
#            else:
#                order[item.name] = quantity
#        except ValueError:
#            print("Invalid input. Please enter a number.")

# The program will print the receipt
# The program will calculate the total price of the order by multiplying the quantity of each item by its price

# Print receipt
#    print("\nReceipt:")
#    total = 0


# The program will itterate through the for loop with the items in the order
# The program will get the price of the item from the menu
# The program will calculate the total price of the item by multiplying the price by the quantity
# The program will add the item total to the total price
# The program will print the item, price, quantity, and item total

#    for item, quantity in order.items():
#        price = menu.items[[menu_item.name for menu_item in menu.items].index(item)].price
#        item_total = price * quantity
#        total += item_total
#        print(f"{item}: ${price} x {quantity} = ${item_total}")
#    print(f"Total: ${total:.2f}")


# Checks if the script is being run directly

#if __name__ == "__main__":
#    main()