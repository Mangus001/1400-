a = float(input("Введите число a: "))
n = int(input("Введите натуральное число n: "))

result = 1.0
for _ in range(n):
    result *= a
print(f"{a} в степени {n} равно {result}")
