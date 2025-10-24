import math
a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))
c = math.sqrt(a ** 2 + b ** 2)
perimeter = a + b + c
print(f"Периметр треугольника: {perimeter:.2f}")
