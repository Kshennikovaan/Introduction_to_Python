# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату x = '))
y = int(input('Введите координату y = '))

if x > 0 and y > 0:
    print('Точка по указанным координатам находится в I квадранте')

elif x < 0 and y > 0:
    print('Точка по указанным координатам находится во II квадранте')

elif x < 0 and y < 0:
    print('Точка по указанным координатам находится в III квадранте')

elif x > 0 and y < 0:
    print('Точка по указанным координатам находится в IV квадранте')

elif x == 0:
    print('Точка по указанным координатам находится на ox')

elif y == 0:
    print('Точка по указанным координатам находится на oy')