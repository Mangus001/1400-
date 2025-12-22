def gcd_three(a, b, c):
    return gcd(gcd(a, b), c)

print(gcd_three(12, 18, 24))
