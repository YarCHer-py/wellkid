import random
a = ["ножницы","камень","бумага"]
computer = random.choice(a)
g =input("Давай сыграем в игру камень ножницы бумага! Напиши предмет: ")
print("Вы выбрали",g +" компьютер выбрал",computer )