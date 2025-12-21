mass = [float(input()) for _ in range(20)]
volume = [float(input()) for _ in range(20)]
max_density = 0
max_density_idx = 0
for i in range(20):
    density = mass[i] / volume[i]
    if density > max_density:
        max_density = density
        max_density_idx = i
print("Максимальная плотность", max_density)
