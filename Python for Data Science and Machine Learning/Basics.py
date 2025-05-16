#x() is the function, weather input or output function,
# Python is the case-sensitive language
from numpy.testing.print_coercion_tables import print_new_cast_table

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
print({'name': 'Swarooop', 'gender':'Male', 'Weight':62})

# type
print(type(3))
print(type('String'))
print(type(2.5))
print(type(3+3j))       # i is not allowed in complex number
print(type([1,2,3]))

# Variables    (Containers for future use)

name = 'Swaroop'
print(name)

a=5
b=7

print(a + b)

# Dynamic Typing i.e python understands data types for the variable
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
