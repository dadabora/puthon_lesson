# построение таблицы
a = 0
b = 0
c = 0
d = 0
e = 0

list_data = []
len_list_data = len(list_data)

while True:
    a_s = 0
    a += 1
    print('Заполните таблицу :     как закончите создавать таблицу, введите в название команду "анализ" ')
    b = input('Название ')
    if b == 'анализ':
        break
    c, d, e = input('Цена '), input('Кол-во '), input('Ед.измерения ')
    data = {"Название": b, "Цена": c, "Количество": d, "Ед.": e}
    number_data = (a, data)
    list_data.append(number_data)
    len_list_data = len(list_data)
    while a_s != len_list_data:
        print(list_data[a_s])
        a_s += 1

# анализ
list_name = []
list_cost = []
list_kol = []
list_izm = []
list_korteg2 = []
while a_s != len_list_data:
    korteg = list_data[a_s]
    print(korteg)
    korteg2 = korteg[1]
    print(korteg2)
    list_name.append(korteg2['Название'])
    list_cost.append(korteg2['Цена'])
    list_kol.append(korteg2['Количество'])
    list_izm.append(korteg2['Ед.'])
    a_s += 1
print('Название :', (list_name))
print('Цена :', (list_cost))
print('Количество :', (list_kol))
print('Ед. :', set(list_izm))
