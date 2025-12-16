def sum_divs(n):
    s = 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

for a in range(2, 50000):
    b = sum_divs(a)
    if b > a and b < 50000:
        if sum_divs(b) == a:
            print((a, b))
