digits = [int(d) for d in number_str]
max_digit = max(digits)
count_max = 0
for d in digits:
    if d == max_digit:
        count_max += 1
