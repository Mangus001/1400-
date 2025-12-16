def digital_root(n):
    while n > 9:
        s = 0
        for ch in str(n):
            s += int(ch)
        n = s
    return n
print(digital_root(9876))
