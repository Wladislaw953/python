a = int(input("Введите сторону прямоугольника a : "))
b = int(input("Введите сторону прямоугольника b : "))
def rectangle(a, b):
    if a > b:
        print('Квадрат ', b,' на ', b)
        return rectangle(a-b,b) + rectangle(a,a)
    elif a < b:
        print('Квадрат ', a,' на ', a)
        return rectangle(b-a, a) + rectangle(b, b)
    else:
        return 1
print("Количество квадратов = ", rectangle(a,b))

