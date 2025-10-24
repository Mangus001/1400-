for b in range(1, 10): 
    for a in range(0, 10):
        c = 546 - 100 * b - 10 * a
        if 0 <= c <= 9:
            x = 100 * a + 10 * b + c
            print(f"b={b}, a={a}, c={c}, x={x}")
