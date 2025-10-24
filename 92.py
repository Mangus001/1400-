for d in range(10):
    min_n = (100 + 999*d + 9) // 10  
    max_n = (999 + 999*d) // 10
    for n in range(min_n, max_n + 1):
        x = 10 * n - 999 * d
        if 100 <= x <= 999:
            if x % 10 == d:
                print(f"Данное n: {n}")
                print(f"x: {x}")
