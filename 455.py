def all_digits_same(n):
    s = str(n)
    return all(d == s[0] for d in s)
