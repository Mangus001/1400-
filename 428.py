max_digit = -1
count_max = 0
for d in number_str:
    d_int = int(d)
    if d_int > max_digit:
        max_digit = d_int
        count_max = 1
    elif d_int == max_digit:
        count_max += 1
