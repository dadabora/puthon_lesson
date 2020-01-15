def my_func(a):
    a = a.title()
    return a


i = str(input('Введите текст'))
text_i = i.split()
text_a = ''
for d in range (len(text_i)):
    slovo = my_func(text_i[d])
    text_a = text_a + ' ' + slovo

print(text_a)