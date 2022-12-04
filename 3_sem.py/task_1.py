#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
#['ssss', 'sngujn556', 56] -> Yes
#['56', 'sgnbsb'] -> No


spisok = ['123', 1.1 , 'sos', '!!!', '__']

n = 0
for i in spisok:

    if type(i) == int or type(i) == float:
        n += 1
if n > 0:
    print('Yes') 
else:
    print('No')
