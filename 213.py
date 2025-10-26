x = float(input())
y = float(input())

max_value = x if x > y else y
min_value = y if y < x else x
print(max_value, min_value)

max_value = x if x > y else y
min_value = x if x < y else y
print(max_value, min_value)
