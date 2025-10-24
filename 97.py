for a in range(1, 10):
    for c in range(0, 10):
        b = 456 - 100 * a - 10 * c
        if 0 <= b <= 9:
            x = 100 * a + 10 * b + c
            print(f"a={a}, b={b}, c={c}, x={x}")
