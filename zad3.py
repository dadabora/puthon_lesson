def first_func(var_1, var_2, var_3):
    arg1 = [var_1, var_2, var_3]
    max1 = int(max(arg1))
    arg1.remove(max1)
    max2 = int(max(arg1))

    return max1 + max2


print(first_func(10, 20, 30))