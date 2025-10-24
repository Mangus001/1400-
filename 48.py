import math

a = float(input("Введите длину большего основания a: "))
b = float(input("Введите длину меньшего основания b: "))
alpha_deg = float(input("Введите угол при большем основании в градусах: "))

alpha = math.radians(alpha_deg)

h = ((b - a) / 2) * math.tan(alpha)

area = ((a + b) / 2) * h

print(f"Площадь трапеции: {area:.2f}")
