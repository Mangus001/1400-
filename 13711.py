def discriminant(a, b, c):
    return b**2 - 4*a*c

def has_real_roots(a, b, c):
    return discriminant(a, b, c) >= 0

a, b, c = 1, -3, 2  
print("Первая:", has_real_roots(a, b, c))
print("Вторая:", has_real_roots(b, a, c))
print("Третья:", has_real_roots(c, a, b))
