a = [float(input()) for _ in range(15)]
a_sorted = sorted(a)
n_input = float(input())
closest_idx = None
closest_val = None
min_diff = float('inf')
for i, val in enumerate(a_sorted):
    diff = abs(val - n_input)
    if diff < min_diff:
        min_diff = diff
        closest_idx = i + 1
        closest_val = val
print(closest_idx, closest_val)
