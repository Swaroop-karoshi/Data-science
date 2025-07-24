# Logical Operators

# or = at least one condition must be True

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled")

# and = both the condition must be true

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold Outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm Outside")
    print("It is Sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is Cold Outside")
    print("It is Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm Outside")
    print("It is Cloudy")