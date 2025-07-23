unit = input("Is this temperature in celsius or Fahrenheit? (C/F): ")
temp = float(input("What is the temperature: "))

if unit == "C":
    temp = (temp * 9 / 5) + 32
    print("The temperature in Fahrenheit is", temp)
elif unit == "F":
    temp = (temp - 32) * 5/9
    print("The temperature in Celsius is", temp)
else:
    print(f"{unit} is an invalid unit")
