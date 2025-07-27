name=input("Enter your name without any space: ")

while name=="":
    print("Enter your name again")
    name=input("Enter your name: ")

print(f"Your name is {name}")

age = int(input("Enter your age: "))

while age<0:
    print("Enter your age again")
    age=int(input("Enter your age: "))

print(f"Your age is {age} years old")

food = input("Enter your favourite food (q to quit): ")

while not food=="q":
    print(f"Your favourite food is {food}")
    food=input("Enter your another favourite food (q to quit): ")
print("Quit successful")

num = int(input("Enter a number between 1 and 10: "))

while num<1 or num>10:
    print("Enter a number not between 1 and 10")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {num}")

