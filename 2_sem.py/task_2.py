# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


number = int(input('Введите число: '))
result = 1
print(result)
for i in range(number):
    result*=-3
    print(result)

