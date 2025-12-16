digits = [int(d) for d in str(n)]
max_digit = max(digits)
min_digit = min(digits)
pos_max_end = pos_max_start = pos_min_end = pos_min_start = 0
for i, d in enumerate(digits):
    if d == max_digit:
        pos_max_start = i + 1
        pos_max_end = len(digits) - i
    if d == min_digit:
        pos_min_start = i + 1
        pos_min_end = len(digits) - i
print(pos_max_end, pos_max_start, pos_min_end, pos_min_start)
