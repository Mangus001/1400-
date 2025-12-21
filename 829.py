n = int(input("Введите n: "))
a, b = map(int, input("Введите a и b: ").split())
array_n = [random.randint(a, b) for _ in range(n)]
print(array_n)
