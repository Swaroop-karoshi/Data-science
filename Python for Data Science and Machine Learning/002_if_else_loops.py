import math
import keyword
import random
import datetime

email  = input("Enter the Email: ")
password = input('Enter the password: ')

if email == 'someone@gmail.com' and  password == '1234':
    print('Welcome')
elif email == 'someone@gmail.com' and  password != '1234':
    print('Incorrect password')
    password = input('Re-Enter the password')
    if password == '1234':
        print('Welcome')
    else:
        print('Password entered is incorrect, Try again later')
else:
    print('Your entered email or password is incorrect')

# Minimum of Three Numbers

a = int(input('First Number: '))
b = int(input('Second Number: '))
c = int(input('Third Number: '))

if a<b and a<c:
    print('Smallest is ', a)
elif b<c:
    print('Smallest is ', b)
else:
    print('smallest is ', c)

# Menu driven Calculator

fnum = int(input("Enter the First Number"))
snum = int(input("Enter the Second Number"))

op = input("Enter the operation")

if op == '+':
    print(fnum + snum)
elif op == '-':
    print(fnum - snum)
elif op == '*':
    print(fnum * snum)
elif op == '/':
    print(fnum / snum)
else:
    print("Operation is not defined")

# Module in python
# 1. Math
# 2. Keywords
# 3. Random
# 4. Datetime

# maths
print(math.factorial(5))
print(math.sqrt(144))

# keyword
print(keyword.kwlist)

# random
print(random.randint(1,100))

# datatime
print(datetime.datetime.now())

# Loops in Python

# Two types of loops
# while loop and for loops
# Looping means repeating something over and over until a particular condition is satisfied

number = int(input("Enter the number: "))

i = 1

while i<11:
    print(number,"*",i,"=",number*i)
    i += 1

# while loop with else

y = 1
while y < 3:
    print(y)
    y += 1
else:
    print("limit crossed")


# Guessing Game

# generate a random integer from 1 and 100

jackpot = random.randint(1,100)

guess = int(input("Guess the Number: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")

    guess = int(input("Guess the Number: "))
    counter += 1
else:
    print("Correct guess")
    print("attempts ", counter)

# For loop demo

for i in range(1, 11):
    print(i)                # here output will be 1 to 10

for i in range(1, 11, 4):   # here 4 specifies intervals
    print(i)                # here output will be 1, 5, 9

for i in range(10, 0, -1):  
    print(i)                # here output will be 10 to 1

