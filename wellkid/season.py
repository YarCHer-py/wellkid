month = int(input("Введите номер месяца : "))
if month == 12 or month <=2 :
    print("Сейчас зима")
elif month <= 5 :
    print("Сейчас весна")
elif month <= 8 :
    print("Сейчас лето! УРА!")
else :
    print("Сейчас осень")