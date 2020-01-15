vvod = []
a = 0
while True:
    a_list = input('Введите числа разделенные пробелом, '
                   'завершение операции по знаку "*" : ').split()
    i = 0

    for i in range(len(a_list)):
        # проверка на выход
        if a_list[i] == '*':
            print('Завершение программы')
            a = 1
            break
        try:
            a_list[i] = int(a_list[i])
            vvod.append(a_list[i])
            i += 1

        except ValueError:
            print('Это не цифра', a_list[i], 'будет удалена из сумирования')

    if a == 1:
        break

    sum_vvod = sum(vvod)
    print(sum_vvod)
sum_vvod = sum(vvod)
print(sum_vvod)