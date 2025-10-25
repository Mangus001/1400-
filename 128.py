import math

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D > 0:
    sqrt_D = math.sqrt(D)
    x1 = (-b + sqrt_D) / (2 * a)
    x2 = (-b - sqrt_D) / (2 * a)
    print("Корни уравнения:", x1, x2)
elif D == 0:
    print("Действительных различных корней нет")
else:
    print("Нет действительных корней")
