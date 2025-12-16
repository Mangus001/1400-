n = int(input())
digits = [int(d) for d in str(n)]
max_odd = -1
index_min_from_left = -1
for i, d in enumerate(digits):
    if d % 2 == 1 and d > max_odd:
        max_odd = d
    if index_min_from_left == -1:
        min_digit = d
        index_min_from_left = i
    else:
        if d < min_digit:
            min_digit = d
            index_min_from_left = i
print(max_odd)
print(index_min_from_left + 1)
