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

