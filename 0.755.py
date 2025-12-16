for b in range(11):
    for k in range(21):
        t = 100 - b - k
        if 0.5 * t + 5 * k + 10 * b == 100:
            print(b, k, t)
