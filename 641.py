masses = [float(input()) for _ in range(n)]
max_mass = max(masses)
min_mass = min(masses)
print(max_mass > 2 * min_mass)
