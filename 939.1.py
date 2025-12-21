birth_years = [random.randint(1950, 2000) for _ in range(30)]
max_year = max(birth_years)
min_year = min(birth_years)
first_oldest_idx = birth_years.index(max_year) + 1
last_oldest_idx = len(birth_years) - 1 - birth_years[::-1].index(max_year)
print(first_oldest_idx, last_oldest_idx)
