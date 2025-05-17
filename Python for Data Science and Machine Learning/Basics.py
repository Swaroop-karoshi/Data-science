# x() is the function, weather input or output function,
# Python is the case-sensitive language
from cgi import print_environ_usage
from xml.dom.minidom import ProcessingInstruction

print("Hello world")

#print(hello world) is wrong because it is string

print(7)
print(1.7)
print(True)                               # "T" should be Capital in True
print("hello", 7, 1.7, True)              # Here space is shown between the output
print('hello', 2, 7.7, True, sep='/')     # Here there is / between
print('Hello', end='-')                   # By-Default there is /n in end so the next print is shown in next line
print('world')                            # By adding - in end the output is shown in same line the - at the end of hello

# DATA TYPES

#integers
print(8)
print(1e308)        # This means 10^308 is the maximum value that can be calculated by python
print(1e309)        # This output is shown as inf which is infinite

# Decimal / float
print(8.55)
print(1.7e308)
print(1.7e309)

# Boolean
print(True)
print(False)

# Text / String
print('hello world')

# complex number
print(5+6j)

# List -> C -> Array
print([1,2,3,4,5])

#Tuple
print((1,2,3,4,5))

# Sets
print({1,2,3,4,5})

# Dictionary
print({'name': 'Swaroop', 'gender':'Male', 'Weight':62})

# type
print(type(3))
print(type('String'))
print(type(2.5))
print(type(3+3j))       # 'i' is not allowed in complex number
print(type([1,2,3]))

# Variables    (Containers for future use)

name = 'Swaroop'
print(name)

a=5
b=7

print(a + b)

# Dynamic Typing i.e. python understands data types for the variable
a=5
# Static Typing
# int a = 5 which is not used in python

# Dynamic Binding

s=4
print(s)
s='swaroop'
print(s)

# Method 1
a = 1
b = 2
c = 3
print(a, b, c)

# Method 2
a,b,c = 1,2,3
print(a,b,c)

a=b=c=5
print(a, b, c)

# Keywords & Identifiers
# Keywords

# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# Given above are the 35 keywords of Python which shouldn't be used as a Variable

# Identifiers
#You can't start with a digit
name1='swaroop'
print(name1)

# You can use special char -> _ (Underscore)
_='swaroop'
print(_)
# identifiers can't be any keywords


# User Input

# Static v/s Dynamic Software
# Static doesn't interact

input('Enter your name:')
input('Enter email:')

# take input from user and store them in a variable
fnum = input('Enter the first number ')
snum = input('Enter the second number ')
print(type(fnum), type(snum))
# add the 2 variables
result = fnum+snum
# print the result
print(result)
# Here the output will be in string that is if we add 45 and 45 here output will be 4545 because input default is string

# Implicit Vs Explicit
# Implicit
print(5+5.6)
print(type(5), type(5.6))

# Explicit
print(int('4'))        # str --> int
print(type(int('4')))
print(int(4.5))        # Here output will be 4
# int(4+5j)     # is error because it is not possible to cinvert to int

# int to string

print(str(5))
print(type(str(5)))

#Float

print(float(4))     # Here output is 4.0

# Take input from user and store them in a variable
fnum = input("Enter first number: ")
snum = input("Enter Second number: ")
# add two variables
result = int(fnum) + int(snum)
print(result)
print(type(fnum))

# Literals
a = 0b1010      # Binary Literal
b = 100         # Decimal Literal
c = 0o310       # Octal Literal
d = 0x12c       # Hexadecimal Literal

print(a,b,c,d)
# Float literal
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-2

print(float_1, float_2, float_3)

# Complex Literal
x = 3.15j
print(x)
print(x.real)
print(x.imag)

string = 'This is Python'
string_12 = "This is Python"
char = "c"
multiline_str = """This is the multiline string with more than
one line of code"""
unicode = u"\U0001f600\U0001f606\U0001f923"
raw_str = r"raw \n string"
not_raw_str = "raw \n string"

print(string)
print(string_12)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
print(not_raw_str)

# Special feature of boolean in mathematics

a = True + 4        # True = 1
b = False +10       # false = 0

print("a: ", a)
print("b: ", b)

a = None
print(a)        # print as None

# Operators

# Arithmatic Operator

print(5+6)
print(5-11)
print(5*7)
print(5/2)
print(5//2)
print(5**2)
print(5%2)

# Relational Operators

print(4>5)
print(4<5)
print(4<=4)
print(4>=4)
print(4==5)
print(4!=4)

# Logical Operators

print(1 and 0)
print(1 or 0)
print(not 1)        # output will be False

# Bitwise Operators

print(2&3)    # This coverts 2 and 3 into binary number and apply and operator in it
print(2|3)
# We know that 2 = 010, and 3 = 011 if we use & operator we get 010 which is 2
# if we use or operator in same we got 011 which is 3

# bitwise xor
print(2 ^ 3)    # In xor operator if both are same then it returns as 0 and if both are different then it returns 1

# in above example 010 and 011 the answer of xor in binary will be 001 which gives 1 as output

# not

print(~6)       # 6 = 110 and NOT 6 = 001 and 1st compliment = 110 and 2nd compliment = 110 + 1 = 111 which is equal to 7 and Not of positive value will be negative so answer will be -7

print(~7)

# Let's solve this
# 7 = 111
# NOT 7 = 000
# 1st compliment = 111
# 2nd compliment = 111 + 1 = 1000
# which is equal to 8 and since in question number is positive then answer should be negative
# Answer is Negative of 8 which is -8

print(4 >> 2)       # Bitwise left operators

print(5<<2)         # Bitwise Right operators

# Assignment Operators

a = 2

a += 2      # a = a + 2

print(a)    # here output will be 4

# you can use -, *, /, %, //, ** also instead of +

# Membership Operator
# in / not in

print('D' in 'Delhi')           # Output is true

print('D' not in 'Delhi')       # Output is False

print(1 in [2,3,4,5,6])         # Output is False

# PROGRAM - Find the sum of a 3 digit entered by the user

number = int(input("Enter the Three digit number: "))

a = number % 10

number = number // 10

b = number % 10

number = number // 10

c = number % 10

print("The sum of 3 digits is: ", a+b+c)