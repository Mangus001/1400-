x1_left_bottom = float(input())
y1_left_bottom = float(input())
width1 = float(input())
height1 = float(input())

x2_left_bottom = float(input())
y2_left_bottom = float(input())
width2 = float(input())
height2 = float(input())

x1_right_top = x1_left_bottom + width1
y1_right_top = y1_left_bottom + height1

x2_right_top = x2_left_bottom + width2
y2_right_top = y2_left_bottom + height2

x_left = min(x1_left_bottom, x2_left_bottom)
y_bottom = min(y1_left_bottom, y2_left_bottom)
x_right = max(x1_right_top, x2_right_top)
y_top = max(y1_right_top, y2_right_top)

print("Координаты левого нижнего угла:", (x_left, y_bottom))
print("Координаты правого верхнего угла:", (x_right, y_top))
