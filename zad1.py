def s_calc():
    try:
        r_val = float(input("Укажите делимое: "))
        h_val = float(input("Укажите делитель: "))
    except ValueError:
        s_full = 'Нужно вводить цифры'
        return s_full
    if h_val == 0:
        s_full = 'На ноль не делиться'
        return s_full
    s_full = r_val / h_val

    return s_full

print(s_calc())
