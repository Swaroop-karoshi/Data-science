# x() is the function, weather input or output function,
# Python is the case-sensitive language
from cgi import print_environ_usage

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

