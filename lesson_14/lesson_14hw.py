shelf1 =['Гарри Поттер', 'Властелин колец']
shelf2 =["Алиса в стране чудес","фантастические существа"]
shelf3 =["Миллион приключений","Война и мир"]
closet =[shelf1,shelf2,shelf3]
closet.append(["Девочка с Земли","Приключения Васи Куролесова"])
print(closet[0][1])
for shelf in closet:
    print(shelf)