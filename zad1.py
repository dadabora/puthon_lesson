list_tips = [1234, 'Тарталетки', True, 1.234,
             [1, 2, 3, 4, 5], (1, 2, 3, 4, 5),
             None, {'a':1, 's':2, "byba":"tyty"},
             {'k', '!', 'r', 'b', 'a', 'd'}, ]
long = len(list_tips)
print(long)
print(list_tips[1])
a = 0
while a != long:

    print(a+1, 'Класс (', list_tips[a], ') =', type(list_tips[a]))
    a += 1
