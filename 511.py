population = [int(input()) for _ in range(12)]
area = [float(input()) for _ in range(12)]
total_population = sum(population)
total_area = sum(area)
density = total_population * 1000 / total_area
print(density)
