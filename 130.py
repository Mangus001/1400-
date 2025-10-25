import math

area_circle = float(input())
area_square = float(input())

radius = math.sqrt(area_circle / math.pi)
side = math.sqrt(area_square)

circle_in_square = (2 * radius) <= side

diagonal_square = side * math.sqrt(2)
square_in_circle = diagonal_square <= 2 * radius

print("Круг уместится в квадрате:", "да" if circle_in_square else "нет")
print("Квадрат уместится в круге:", "да" if square_in_circle else "нет")
