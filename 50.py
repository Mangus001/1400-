x1, y1 = map(float, input("Введите координаты вершины 1 (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты вершины 2 (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты вершины 3 (x3 y3): ").split())
x4, y4 = map(float, input("Введите координаты вершины 4 (x4 y4): ").split())

def triangle_area(xa, ya, xb, yb, xc, yc):
    return 0.5 * abs(xa*(yb - yc) + xb*(yc - ya) + xc*(ya - yb))

area1 = triangle_area(x1, y1, x2, y2, x3, y3)
area2 = triangle_area(x1, y1, x3, y3, x4, y4)

total_area = area1 + area2

print(f"Площадь четырехугольника: {total_area:.2f}")
