import math

R_outer = float(input("Введите внешний радиус: "))

R_inner = float(input("Введите внутренний радиус: "))

if R_inner >= R_outer:
    print("Внутренний радиус должен быть меньше внешнего радиуса.")
else:
    area = math.pi * (R_outer ** 2 - R_inner ** 2)
    print(f"Площадь кольца: {area:.2f}")
