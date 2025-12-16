population = [int(input()) for _ in range(12)]
density = [float(input()) for _ in range(12)]
total_area = sum([population[i] * 1000 / density[i] for i in range(12)])
print(total_area)
