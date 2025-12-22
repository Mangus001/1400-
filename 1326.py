countries = [("Country1", pop1, area1), ("Country2", pop2, area2)]
densities = [pop/area for _, pop, area in countries]
max_density = max(densities)
