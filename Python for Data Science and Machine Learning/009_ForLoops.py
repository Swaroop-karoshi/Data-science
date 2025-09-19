# for loops

for i in range(1, 11):
    print(i)
print("bye")

for i in reversed((1, 11)):
    print(i)

for i in range(1, 11, 2):       #This give the 2 step after the initial
    print(i)

debit_card = "1234-5678-9123-4567"

for i in debit_card:
    print(i)

for x in range(1, 21):
    if x == 12:
        break
    else:
        print(x)

for x in range(1, 21):
    if x == 12:
        continue
    else:
        print(x)
