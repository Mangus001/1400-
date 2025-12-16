def is_digits_increasing_from_left(n):
    s = str(n)
    return all(s[i] < s[i+1] for i in range(len(s)-1))
