import math
def coprimes(n):
    result = []
    for x in range(1, n):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        if gcd(x, n) == 1:
            result.append(x)
    return result
