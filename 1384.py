def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes_three_digits = [n for n in range(100, 1000) if is_prime(n)]
print("Трехзначные простые числа:", primes_three_digits)
