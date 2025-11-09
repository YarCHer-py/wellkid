from random import randint

# Задать случайные значения тоду
tod_room = randint(1, 10)
tod_corner = randint(1, 4)
tod_is_found = False
# Организовать 2 вложенных цикла
for room in range(1, 11):
    for corner in range(1, 5):
        # Если нашли тода то вывести соответствующее сообщение и выйти из цикла
        if tod_room == room and tod_corner == corner:
            print(f"Тод найден в комнате {room} в углу под номером {corner}")
            tod_is_found = True
            break
    if tod_is_found:
        break
    print(f"error 404: tod not found in room {room}")
