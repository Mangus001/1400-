a = float(input("Введите число a: "))
n = int(input("Введите целое n: "))

result = 1.0
for _ in range(n):
    result *= a
print(f"{a} в степени {n} равно {result}")
