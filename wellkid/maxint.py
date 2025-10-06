def input_num() :
    num1 = int(input())
    while num1 >=1000000000:
        print("Число должно быть меньше чем 10^9! Введите ещё раз!")
        num1= int(input())
    return num1

big = 1
num = input_num()
while num != 0:
    if num > big :
        big = num
    num = input_num()
print(big)

