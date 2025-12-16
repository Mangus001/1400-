x = list(map(int, input().split()))
max1 = max2 = float('-inf')
min1 = min2 = float('inf')
max_idx1 = max_idx2 = -1
min_idx1 = min_idx2 = -1
for i in range(len(x)):
    if x[i] > max1:
        max2 = max1
        max_idx2 = max_idx1
        max1 = x[i]
        max_idx1 = i
    elif x[i] > max2:
        max2 = x[i]
        max_idx2 = i
    if x[i] < min1:
        min2 = min1
        min_idx2 = min_idx1
        min1 = x[i]
        min_idx1 = i
    elif x[i] < min2:
        min2 = x[i]
        min_idx2 = i
print(max_idx1 + 1, max_idx2 + 1)
print(min_idx1 + 1, min_idx2 + 1)
