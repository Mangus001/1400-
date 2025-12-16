import math

def sum_divisors(n):
    s = 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

n = 6
while n < 100000:
    if sum_divisors(n) == n:
        print(n)
    n += 1
