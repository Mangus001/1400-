def coprime_divisors(q, p):
    divisors = []
    for d in range(1, q + 1):
        if q % d == 0:
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a
            if gcd(d, p) == 1:
                divisors.append(d)
    return divisors
