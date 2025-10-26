# а) полусумма абсолютных величин
x = float(input())
y = float(input())
abs_x = x if x >= 0 else -x
abs_y = y if y >= 0 else -y
half_sum = (abs_x + abs_y) / 2
print(half_sum)
