import math

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

arithmetic_mean = (a + b) / 2

if a >= 0 and b >= 0:
    geometric_mean = math.sqrt(a * b)
else:
    geometric_mean = None 

print(f"Среднее арифметическое: {arithmetic_mean}")

if geometric_mean is not None:
    print(f"Среднее геометрическое: {geometric_mean}")
else:
    print("Среднее геометрическое не определено для отрицательных чисел.")
