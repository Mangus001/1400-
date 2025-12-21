temps_july = [random.uniform(15, 35) for _ in range(31)]
min_temp = min(temps_july)
cold_days = sum(1 for t in temps_july if t == min_temp)
print(cold_days)
