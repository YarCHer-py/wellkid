from random import *
num = randint(1,100)
num_pol = int(input("Угадай число! от 1 до 100! "))
while num != num_pol:
    print("Не угадал!")
    if num > num_pol:
        print("Моё число Больше!")
    else:
        print("Моё число меньше!")
    num_pol = int(input("Попробуй ещё раз! "))
print("Молодец ты угадал!!!!")