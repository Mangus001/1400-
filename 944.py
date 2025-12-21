rain_october = [random.uniform(0, 50) for _ in range(31)]
max_rain = max(rain_october)
max_days = sum(1 for x in rain_october if x == max_rain)
print(max_days)
