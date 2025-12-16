m = int(input("Введите значение m: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
k = random.randint(1, m)
print(f"Случайное число k: {k}")
for _ in range(k):
    ni = a + random.random() * (b - a)
    print(ni)
