def has_adjacent_duplicate(n):
    s = str(n)
    return any(s[i] == s[i+1] for i in range(len(s)-1))
