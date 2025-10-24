import math

x1, y1 = map(float, input("Введите координаты первой вершины (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй вершины (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты третьей вершины (x3 y3): ").split())

def distance(xa, ya, xb, yb):
    return math.sqrt((xb - xa)**2 + (yb - ya)**2)

d_AB = distance(x1, y1, x2, y2)
d_BC = distance(x2, y2, x3, y3)
d_CA = distance(x3, y3, x1, y1)

perimeter = d_AB + d_BC + d_CA

area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

print(f"Периметр треугольника: {perimeter:.2f}")
print(f"Площадь треугольника: {area:.2f}")
