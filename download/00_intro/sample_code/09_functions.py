def mult_and_abs(x, y):
    z = x * y

    if z >= 0:
        return z
    else:
        return z * -1


print(mult_and_abs(-3, 2))