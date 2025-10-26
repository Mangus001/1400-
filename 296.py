n = int(input("Введите n (1 ≤ n ≤ 100): "))
total = sum(i ** 2 for i in range(1, n + 1))
print(total)
