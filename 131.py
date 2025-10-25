import math

area_circle = float(input())
area_triangle = float(input())

radius = math.sqrt(area_circle / math.pi)

side_triangle = math.sqrt((4 * area_triangle) / math.sqrt(3))

radius_in_triangle = (side_triangle * math.sqrt(3)) / 6
circle_in_triangle = radius <= radius_in_triangle

triangle_in_circle = side_triangle <= 2 * radius

print("Круг уместится в треугольнике:", "да" if circle_in_triangle else "нет")
print("Треугольник уместится в круге:", "да" if triangle_in_circle else "нет")
