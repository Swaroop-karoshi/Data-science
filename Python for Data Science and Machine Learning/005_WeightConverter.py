weight = float(input("Enter the weight: "))
unit = input("Enter the unit that you want to convert (K, L): ")

if unit == "K":
    weight = round(weight / 2.205, 3)
    print("The weight is", weight, "Kg")
elif unit == "L":
    weight = round(weight * 2.205, 3)
    print("The weight is", weight, "lb")
else:
    print("Operation not supported")