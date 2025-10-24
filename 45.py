a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

volume = a * b * c

lateral_surface_area = 2 * (a * b + a * c + b * c)

print(f"Объем параллелепипеда: {volume}")
print(f"Площадь боковой поверхности: {lateral_surface_area}")
