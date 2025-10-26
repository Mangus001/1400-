a = int(input("Введите a (0 ≤ a ≤ 50): "))
total = sum(i ** 2 for i in range(a, 51))
print(total)
