def simplify_fraction(a, b):
    divisor = gcd(a, b)
    return a // divisor, b // divisor

a, b = 8, 12
p, q = simplify_fraction(a, b)
print(f"Сокращенная дробь: {p}/{q}")
