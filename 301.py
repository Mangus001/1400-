n = int(input("Введите n (n ≥ 2): "))
total = sum(i * (i + 1) for i in range(1, n))
print(total)
