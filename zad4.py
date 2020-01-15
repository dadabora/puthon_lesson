def my_func():
    x = int(input('Введите х: '))
    y = int(input('Введите y: '))
    return x**y
print(my_func())

def my_func1():
    x = int(input('Введите х: '))
    y = int(input('Введите y: '))
    a = 0
    xoy = 1
    b = abs(y)
    if y == 0:
        return xoy
    while a != b:
        a += 1
        xoy = xoy*x
    if y < 0:
            xoy = 1/xoy


    return xoy
print(my_func1())