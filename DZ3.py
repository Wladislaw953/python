"""3. Торговая фирма в первый день работы реализовала товаров на P тыс. руб.,
а затем ежедневно увеличивала выручку на 3%.
Какой будет выручка фирмы в тот день, когда она впервые превысит заданное значение Q?
Сколько дней придется торговать фирме для достижения этого результата?"""

p = int(input("Введите сумму за реализованный товар в первый день: \n"))
q = int(input("Задайте значение выручки: \n"))
den = 1
while p <= q:
    den += 1
    p += 0.03 * p
print("Выручка: " + str(p))
print("Ориентировочное количество дней: " + str(den))