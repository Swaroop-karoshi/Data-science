Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the Second number: "))
Operation = input("Enter the operation (+, -, *, /): ")

if Operation == "+":
    print("The sum is", round(Num1 + Num2, 3))
elif Operation == "-":
    print("The difference is", round(Num1 - Num2, 3))
elif Operation == "*":
    print("The multiplication is", round(Num1 * Num2, 3))
elif Operation == "/":
    print("The division is", round(Num1 / Num2, 3))
else:
    print("Operation not supported")
