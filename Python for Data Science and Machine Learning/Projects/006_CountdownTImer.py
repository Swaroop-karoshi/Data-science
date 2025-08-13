import time

my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)

print("Time's up!")

# Reversed Method 01

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)

print("Time's up!")

# Reversed Method 02

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print("Time's up!")

# Timer

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")

