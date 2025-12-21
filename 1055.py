population = [some_population_values]
area = [some_area_values]
total_population = 0
total_area = 0
for p, A in zip(population, area):
    if A <= A_threshold:
        total_population += p
        total_area += A
