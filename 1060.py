max_density = 0
max_idx = 0
for i in range(20):
    for j in range(i+1, 20):
        d1 = mass[i] / volume[i]
        d2 = mass[j] / volume[j]
        if d1 > max_density:
            max_density = d1
            max_idx = i
        if d2 > max_density:
            max_density = d2
            max_idx = j
print("Максимальная плотность", max_density)
