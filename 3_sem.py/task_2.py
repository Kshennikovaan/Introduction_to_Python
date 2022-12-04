#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#- список: [], ищем: "123", ответ: -1

# from os import system 
# system("cls")
# stroka = ['kjl', 'lkj', 'lkj', 'lkj', 'lkm']
# t = 0
# p = 0
# pos =0



# n = input('введите значение ')
# while p < 2 and t <len(stroka) - 1:
#    if stroka[t] == n:
#        p += 1
#        pos =t 
#    t += 1
# if p >1:
#    print(pos)
# else:
#    print(-1)



#Второй вариант решения
# mass = ['ssss', 'sngujn556', '44']
# types = [str(type(i)) for i in mass]
# if "<class 'int'>" in types or "<class 'float'>" in types:
#     print('Yes')
# else:
#     print('No')

mass = ["123", "234", 123, "567"]
a = 123
try:
    mass.remove(a)
    print((mass.index(a))+1)
except ValueError:
    print(-1)
