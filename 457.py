def is_digits_non_decreasing_from_right(n):
    s = str(n)[::-1]
    return all(s[i] <= s[i+1] for i in range(len(s)-1))
