import math

radius = float(input())
side = float(input())

area_circle = math.pi * radius ** 2

area_square = side ** 2

result = "круга" if area_circle > area_square else "квадрата"

print(result)
