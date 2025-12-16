def is_power_of_5(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1
