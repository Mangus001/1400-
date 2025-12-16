a = int(input("Введите значение a: "))
b = float(input("Введите значение b: "))

k = random.randint(1, a)
print(f"Случайное число k: {k}")

print("Случайные числа ni:")

for _ in range(k):
    ni = random.random() * b
    print(ni)
  
