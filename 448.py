def is_in_arithmetic_progression(n, f, s):
    if s == 0:
        return n == f
    diff = n - f
    if diff % s == 0 and diff // s >= 0:
        return True
    return False
