#Вариант 9 Найти среднее арифметическое элементов списка
import random
a = int(input('Введите размер списка:\n'))
b = []
for i in range(a):
    c = random.randint(1, 23)
    b.append(c)
s = sum(b)
l = len(b)
c = s/l
print('Элементы списка: ')
for i in range(a):
    print(b[i])
print('Среднее арифметическое элементов:' + str(c))