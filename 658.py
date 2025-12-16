U = list(map(float, input().split()))
R = list(map(float, input().split()))
min_current = float('inf')
min_idx = -1
for i in range(20):
    current = U[i] / R[i]
    if current <= min_current:
        min_current = current
        min_idx = i
print(min_idx + 1)
