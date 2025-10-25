x1_left_bottom = float(input())
y1_left_bottom = float(input())
x1_right_top = float(input())
y1_right_top = float(input())

x2_left_bottom = float(input())
y2_left_bottom = float(input())
x2_right_top = float(input())
y2_right_top = float(input())

x_left = min(x1_left_bottom, x2_left_bottom)
y_bottom = min(y1_left_bottom, y2_left_bottom)
x_right = max(x1_right_top, x2_right_top)
y_top = max(y1_right_top, y2_right_top)

print("Левый нижний угол:", (x_left, y_bottom))
print("Правый верхний угол:", (x_right, y_top))
