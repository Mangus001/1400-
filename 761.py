def prime_divisors(n):
    divisors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            divisors.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    return divisors
