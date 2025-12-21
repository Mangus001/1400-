a = [int(input()) for _ in range(10)]
b = [a[i]**2 if i % 2 == 0 else 2*a[i] for i in range(10)]
