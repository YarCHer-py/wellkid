from random import randint

table = []

for i in range(3):
    a = randint(-100, 100)
    b = randint(-100, 100)
    c = randint(-100, 100)
    table.append([a, b, c])
print(table)

for i in range(1, 4):
    for j in range(1, 4):
        v = randint(-100, 100)
    if v > 0:
        print("позитивное")
    elif v == 0:
        print("ноль")
    else:
        print("отрицательное")
    table.append([v])
