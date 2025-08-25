# Shopping Cart Program

food = []
prices = []
total_price = 0

while True:
    food = input("Enter the food you would like to purchase(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))