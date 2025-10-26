x = float(input())
y = float(input())
z = float(input())
w = float(input())

max_value = x if x > y else y
max_value = max_value if max_value > z else z
max_value = max_value if max_value > w else w

min_value = x if x < y else y
min_value = min_value if min_value < z else z
min_value = min_value if min_value < w else w

print(max_value)
print(min_value)
