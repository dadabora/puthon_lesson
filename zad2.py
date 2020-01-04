full = 0
list_full = []
while full != "and":
    full = input('Введите значение списка:  ')
    print('Если закончили введите "and"', full)
    if full == 'and':
        break
    list_full.append(full)
print(list_full)

long = len(list_full)

a = 0
b = 1
while a != long:
    if b >= long:
        break
    one = list_full[a]
    two = list_full[b]

    list_full.pop(a)
    list_full.pop(a)


    list_full.insert(a, two)
    list_full.insert(b, one)
    a += 2
    b += 2

print(list_full)
