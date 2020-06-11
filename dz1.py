#WARIANT 4: По номеру месяца напечатать пору года.
a = int(input("Для того что бы узнать пору года, введите номер месяца от 1 до 12: "))
if a > 0 and a <= 2:
    print('Зима')
elif a >= 3 and a <= 5:
    print('Весна')
elif a >= 6 and a <= 8:
    print('Лето')
elif a >= 9 and a <= 11:
    print('Осень')
elif a == 12:
    print('Зима')
else:
    print('Некорректо введён месяц')