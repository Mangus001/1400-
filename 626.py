n = int(input())
x = [float(input()) for _ in range(15)]
max_x = float('-inf')
min_x = float('inf')
for val in x:
    if val > max_x:
        max_x = val
    if val < min_x:
        min_x = val
print(max_x, min_x)
