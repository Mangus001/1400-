n = 100000
inside_circle = 0
for _ in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1
pi_estimate = 4 * (inside_circle / n)
print(f"Pi ≈ {pi_estimate}")
