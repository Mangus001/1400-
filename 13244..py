items = [("предмет1", mass1, volume1), ("предмет2", mass2, volume2)]
densities = [mass/vol for item, mass, vol in items]
max_density = max(densities)
