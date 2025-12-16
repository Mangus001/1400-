masses = [float(input()) for _ in range(20)]
volumes = [float(input()) for _ in range(20)]
densities = [mass / vol for mass, vol in zip(masses, volumes)]
max_density = max(densities)
print(max_density)
