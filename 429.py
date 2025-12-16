min_digit = 10
count_min = 0
for d in number_str:
    d_int = int(d)
    if d_int < min_digit:
        min_digit = d_int
        count_min = 1
    elif d_int == min_digit:
        count_min += 1
