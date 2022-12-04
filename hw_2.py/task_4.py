# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

#with open('file_for_ex4.txt', 'w') as data:
#   data.write('-2\n')
#   data.write('-1\n')
#   data.write('0\n')
#   data.write('1\n')
#   data.write('2\n')

with open('file_for_ex4.txt', 'r') as data:
    pos = data.read().split()
pos = list(map(int, pos))
    
n = int(input())
list_generation = [i for i in range(-n, n + 1)]
mult = 1
for p in pos:
    mult *= list_generation[p]
    
print(pos)
print(list_generation)
print(mult)
