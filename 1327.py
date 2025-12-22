items = [("предмет1", mass1, volume1), ("предмет2", mass2, volume2)]
densities = [mass/vol for _, mass, vol in items]
min_density = min(densities)
