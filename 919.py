ainfalls = [random.uniform(300, 700) for _ in range(15)]
avg_rainfall = sum(rainfalls)/15
deviations = [r - avg_rainfall for r in rainfalls]
print(avg_rainfall, deviations)
