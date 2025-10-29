n = int(input("Введите целое число n: "))
a = float(input("Введите вещественное число a: "))

product = 0.0
for _ in range(n):
    product += a

print(f"{n} * {a} = {product}")
