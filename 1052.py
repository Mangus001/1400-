population = [some_population_value]
area = [some_area_value]
total_population = sum(p for p, A in zip(population, area) if A > 5)
print(total_population)
