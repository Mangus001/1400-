populations = [float(input()) for _ in range(16)]
areas = [float(input()) for _ in range(16)]
densities = [pop / area for pop, area in zip(populations, areas)]
print(min(densities))
