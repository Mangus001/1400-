k = int(input("Введите количество чисел k: "))
print(f"Было сгенерировано {k} случайных чисел:")

for _ in range(k):
    ni = random.random()
    print(ni)
