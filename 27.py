import math

radius = float(input("Введите радиус окружности: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")
