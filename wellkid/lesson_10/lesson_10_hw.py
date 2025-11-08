fruit_list = ['банан', 'яблоко', 'персик', 'гуава']
match = False
a = input("Введите блюдо ")
for i in fruit_list:
    if a == i:
        match = True
        print("Блюдо в всписке есть")
        break
if not match:
    print("Такого блюда в списке нет!")