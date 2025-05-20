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

op = int("Enter the operation")