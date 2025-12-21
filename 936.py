birth_years = [random.randint(1950, 2000) for _ in range(30)]
oldest = min(birth_years)
youngest = max(birth_years)
diff_age = oldest - youngest
print(diff_age)
