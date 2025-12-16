def is_monotonic_left(n):
    s = str(n)
    increasing = all(s[i] < s[i+1] for i in range(len(s)-1))
    decreasing = all(s[i] > s[i+1] for i in range(len(s)-1))
    return increasing or decreasing
