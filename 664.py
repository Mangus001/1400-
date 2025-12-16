results = list(map(int, input().split()))
max1 = max2 = float('-inf')
max_idx1 = max_idx2 = -1
for i in range(22):
    if results[i] > max1:
        max2 = max1
        max_idx2 = max_idx1
        max1 = results[i]
        max_idx1 = i
    elif results[i] > max2:
        max2 = results[i]
        max_idx2 = i
print(results[max_idx1], results[max_idx2])
