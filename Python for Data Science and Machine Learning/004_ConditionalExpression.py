# Conditional Expression
from unicodedata import category

# Single line condition of positive or negative
num = 5

print("Positive" if num > 0 else "Negative")


# single line condition for even or odd

num = 6
result = "Even" if num % 2 == 0 else "Odd"

print(result)

a = 6
b = 7

max_num = a if a>b else b
print(max_num)

min_num = a if a<b else b
print(min_num)

age = 13

category = "adult" if age >= 18 else "Child"
print(category)

user_role = "Admin"

access = "Full Access" if user_role == "Admin" else "Limited Access"
print(access)
