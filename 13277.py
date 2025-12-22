countries = [("Country1", pop1, area1), ("Country2", pop2, area2)]
densities = [pop/area for _, pop, area in countries]
min_density = min(densities)
for name, pop, area in countries:
    if pop/area == min_density:
        print(name)
