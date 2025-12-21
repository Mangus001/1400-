num_points = 10000
inside = 0
for _ in range(num_points):
    x = random.uniform(0, math.pi)
    y = random.uniform(0, 1)
    if y <= math.sin(x) / 2:
        inside += 1
area_a = (math.pi) * 1 * (inside / num_points)

inside_b = 0
for _ in range(num_points):
    x = random.uniform(0, 3)
    y = random.uniform(0, 9)
    if y <= x**2:
        inside_b += 1
area_b = 3 * 9 * (inside_b / num_points)
print(area_a, area_b)
