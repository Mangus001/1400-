n = int(input("Введите n (1 ≤ n ≤ 999): "))

if n % 10 == 0:
    print("Некорректное значение n, в числе ноль в единицах.")
else:
    x_found = None
    for a in range(1, 10):
        for b in range(10):
            c = n - 10 * b
            if 0 <= c <= 9:
                if 100 * c + 10 * b + a == n:
                    x = 100 * a + 10 * b + c
                    x_found = x
                    print(f"Найденное число x: {x}")
                    break
        if x_found is not None:
            break
    if x_found is None:
        print("Число x не найдено.")
