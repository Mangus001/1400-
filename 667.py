import math

# 7.175
n = int(input())
a = list(map(int, input().split()))
min_sum = float('inf')
result = ()
for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            for m in range(k + 1, n):
                s = a[i] + a[j] + a[k] + a[m]
                if s < min_sum:
                    min_sum = s
                    result = (i+1, j+1, k+1, m+1)
print(*result)
