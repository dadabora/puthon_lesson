imba = input('введите слова')
list_imba = imba.split()
print(list_imba)
namber = len(list_imba)
a = 0
while a != namber:
    slovo = list_imba[a]
    a += 1
    print(a, slovo[:10])