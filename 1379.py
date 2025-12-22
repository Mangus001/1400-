def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

vertices = [(0,0), (4,0), (5,3), (2,5), (-1,2)]
print("Площадь многоугольника:", polygon_area(vertices))
