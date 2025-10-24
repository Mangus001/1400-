import math

x1 = float(input("Введите x первой точки: "))
y1 = float(input("Введите y первой точки: "))

x2 = float(input("Введите x второй точки: "))
y2 = float(input("Введите y второй точки: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Расстояние между точками: {distance:.2f}")
