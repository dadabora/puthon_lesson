list_namber = []
while True:
    print(sorted(list_namber, reverse=True))
    namber =input('Введите цифру : ')

    if namber == 'end':
        break

    list_namber.append(int(namber))

    print('Для завершения введите "end"')





