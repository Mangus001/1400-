y = [float(input()) for _ in range(15)]
n = float(input())
index_n = 0
for i in range(15):
    index_n = i if y[i] < n else index_n
sum_less_n = sum(y[i] for i in range(15) if y[i] < n)
lower_idx = 0
upper_idx = 0
for i in range(14):
    if y[i] < n < y[i+1]:
        lower_idx, upper_idx = i+1, i+2
        break
print(sum_less_n)
print(lower_idx+1, y[lower_idx], upper_idx+1, y[upper_idx])
