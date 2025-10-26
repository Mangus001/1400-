x = float(input())
y = float(input())

max_value = x if x > y else y if y > x else x
print(max_value)

max_value = x if x > y else y
print(max_value)
