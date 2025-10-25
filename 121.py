x = float(input())
y = float(input())

max_value = x if x > y else y
min_value = y if y < x else x

print("Максимальное:", max_value)
print("Минимальное:", min_value)
