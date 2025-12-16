n = int(input())
t = list(map(float, input().split()))
c = [0] * n
min_time = t[0]
min_index = 0
for i in range(n):
    c[i] = sum(t[:i+1])
    if t[i] <= min_time:
        min_time = t[i]
        min_index = i
print([round(ci, 2) for ci in c])
print(min_index + 1)
