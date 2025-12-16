def coprime_with_p(n, p):
    result = []
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    for x in range(1, n):
        if gcd(x, p) == 1:
            result.append(x)
    return result
