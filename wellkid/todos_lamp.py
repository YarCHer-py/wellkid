color = int(input("color 1-10 "))
intensity = int(input("intensity 1-3 "))
c=i='undefined'

if color == 1:
    c = "красный"
elif color == 2:
    c = "жёлтый"
elif color == 3:
    c = "зелёный"
elif color == 4:
    c = "чёрный"
elif color == 5:
    c = "фиолетовый"
elif color == 6:
    c = "оранжевый"
elif color == 7:
    c = "голубой"
elif color == 8:
    c = "синий"
elif color == 9:
    c = "коричневый"
elif color == 10:
    c = "белый"

if intensity == 1:
    i = "тусклый"
elif intensity == 2:
    i = "нормальный"
elif intensity == 3:
    i = "яркий"
print(c , i )
