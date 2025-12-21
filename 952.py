ages = [22, 35, 20, 35, 28]
max_age = max(ages)
min_age = min(ages)
first_max_idx = ages.index(max_age)
first_min_idx = ages.index(min_age)
print("Oldest" if first_max_idx < first_min_idx else "Youngest")
