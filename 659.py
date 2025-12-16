n = int(input())
x = list(map(int, input().split()))
max_val = x[0]
max_pos = 0
min_val = x[0]
min_pos = 0
for i in range(1, n):
    if x[i] == max_val and max_pos == 0:
        max_pos = i
    if x[i] > max_val:
        max_val = x[i]
        max_pos = i
    if x[i] == min_val and min_pos == 0:
        min_pos = i
    if x[i] < min_val:
        min_val = x[i]
        min_pos = i
if max_pos < min_pos:
    print("max")
else:
    print("min")
