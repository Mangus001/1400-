n = int(input())
a = []
b = []
for _ in range(n):
    ai, bi = map(float, input().split())
    a.append(ai)
    b.append(bi)
max_avg = -1
max_avg_idx = -1
for i in range(n):
    avg = (a[i] + b[i]) / 2
    if avg >= max_avg:
        max_avg = avg
        max_avg_idx = i
min_gm = float('inf')
min_gm_idx = -1
import math
for i in range(n):
    gm = math.sqrt(a[i] * b[i])
    if gm <= min_gm:
        min_gm = gm
        min_gm_idx = i
print(max_avg_idx + 1, min_gm_idx + 1)
