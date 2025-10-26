a = int(input("Введите a: "))
b = int(input("Введите b (b ≥ a): "))
total = sum(i ** 2 for i in range(a, b + 1))
print(total)
