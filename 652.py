n = int(input())
results = list(map(float, input().split()))
min_time = results[0]
best_index = 0
for i in range(1, n):
    if results[i] < min_time:
        min_time = results[i]
        best_index = i
print(best_index + 1)
