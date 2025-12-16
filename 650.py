n = int(input())
a = [int(input()) for _ in range(n)]
max_val = max(a)
min_val = min(a)
last_max_idx = len(a) - 1 - a[::-1].index(max_val) + 1
first_min_idx = a.index(min_val) + 1
print(last_max_idx)
print(first_min_idx)
