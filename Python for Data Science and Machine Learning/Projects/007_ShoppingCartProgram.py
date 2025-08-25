# Shopping Cart Program

foods = []
prices = []
total_price = 0


while True:
    food = input("Enter the food you would like to purchase(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("--------YOUR CART--------")

for food in foods:
    print(food, end="|")

for price in prices:
    total_price = total_price + price

print()
print(f"Your total is: ${total_price}")
