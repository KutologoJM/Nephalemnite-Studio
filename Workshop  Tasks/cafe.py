"""
Cafe stock value calculator
Lists:
    Menu - contains all available menu items
Dictionaries:
    stock - contains stock quantity for each menu item
    price - contains price for each menu item in Rands

Task:
    Calculate total stock and print result on console
"""
menu = ["Espresso", "Latte", "Muffin", "Sandwich", "Donut", "Frappuccino"]
stock = {"Espresso": 30, "Latte": 50, "Muffin": 30, "Sandwich": 15, "Donut": 50, "Frappuccino": 64}
price = {"Espresso": 70, "Latte": 55, "Muffin": 32, "Sandwich": 35, "Donut": 25, "Frappuccino": 120}
total_stock = 0

# calculates stock value of each available item
for i in range(len(menu)):
    stock_value = stock[menu[i]]
    price_value = price[menu[i]]
    total_stock += stock_value * price_value  # calculates combined value of all available items


print(f"The total stock value for the cafe is R{total_stock}.")
