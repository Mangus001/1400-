def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

twins = []
for n in range(3, 200):
    if is_prime(n) and is_prime(n + 2):
        twins.append((n, n + 2))
print("Пары близнецов:", twins)
