#Format Specifiers

price1= 4000.1684
price2= -9408.48
price3= 120000.046

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.5f}")

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:^10}")

print(f"Price 3 is ${price3:+}")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

print(f"Price 1 is ${price1:+,2f}")
print(f"Price 2 is ${price2:+,2f}")
print(f"Price 3 is ${price3:+,2f}")