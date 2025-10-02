# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.00,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 1.50,
        "lemonade": 3.50}
cart = []
total = 0

print("------- MENU --------")
for key, value in menu.items():
    print(f"{key:13}: ${value:.2f}")

while True:
    food = input("What would you like to pick up? (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------Your Order--------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total: ${total:.2f}")