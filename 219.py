x = float(input())
y = float(input())
abs_x = x if x >= 0 else -x
abs_y = y if y >= 0 else -y
if abs_x > abs_y:
    x /= 2
print(x)
