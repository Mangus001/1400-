for d in range(10):
    remaining = 237 - 100*d
    if 0 <= remaining <= 99:
        a = remaining // 10
        b = remaining % 10
        if 1 <= a <= 9:  # поскольку число трехзначное, а не нулевое
            # проверка выполнена
            x = 100*a + 10*b + d
            print("Число x:", x)
