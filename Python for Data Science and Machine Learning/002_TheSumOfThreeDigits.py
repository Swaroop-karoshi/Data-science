# PROGRAM - Find the sum of a 3 digit entered by the user

number = int(input("Enter the Three digit number: "))

a = number % 10

number = number // 10

b = number % 10

number = number // 10

c = number % 10

print("The sum of 3 digits is: ", a+b+c)

# Program to Generate Fibonacci Sequence of Length N
# Suitable for First-Year Engineering Students

N=int(input("Enter the f number: "))

n1=0
n2=1

print("the f s of", N, "is: ")

for i in range(N):
    print(n1, end=" ")

    n3=n1+n2
    n1=n2
    n2=n3


# Program ends
