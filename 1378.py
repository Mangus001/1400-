def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangle_perimeter(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    return a + b + c

x1, y1 = 0, 0
x2, y2 = 3, 0
x3, y3 = 0, 4
print("Периметр треугольника:", triangle_perimeter(x1, y1, x2, y2, x3, y3))
