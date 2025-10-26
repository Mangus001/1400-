n = int(input("Введите n: "))
total = sum(i ** 2 for i in range(n, 2 * n + 1))
print(total)
