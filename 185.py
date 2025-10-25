x1, y1, w1, h1 = map(float, input("Введите x, y, ширину, высоту первого прямоугольника через пробел: ").split())
x2, y2, w2, h2 = map(float, input("Введите x, y, ширину, высоту второго прямоугольника через пробел: ").split())

points_first = [
    (x1, y1),
    (x1 + w1, y1),
    (x1, y1 + h1),
    (x1 + w1, y1 + h1)
]
points_second = [
    (x2, y2),
    (x2 + w2, y2),
    (x2, y2 + h2),
    (x2 + w2, y2 + h2)
]

def all_points_inside(points, rect_x, rect_y, rect_w, rect_h):
    for (x, y) in points:
        if not (rect_x <= x <= rect_x + rect_w and rect_y <= y <= rect_y + rect_h):
            return False
    return True
  
all_first_in_second = all_points_inside(points_first, x2, y2, w2, h2)
all_second_in_first = all_points_inside(points_second, x1, y1, w1, h1)

x_min1, x_max1 = x1, x1 + w1
y_min1, y_max1 = y1, y1 + h1

x_min2, x_max2 = x2, x2 + w2
y_min2, y_max2 = y2, y2 + h2

intersect = not (x_max1 < x_min2 or x_max2 < x_min1 or y_max1 < y_min2 or y_max2 < y_min1)

print(f"Все точки первого внутри второго: {'Да' if all_first_in_second else 'Нет'}")
print(f"Все точки второго внутри первого: {'Да' if all_second_in_first else 'Нет'}")
print(f"Прямоугольники пересекаются: {'Да' if intersect else 'Нет'}")
