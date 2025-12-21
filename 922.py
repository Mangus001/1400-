temperatures = [random.uniform(15, 35) for _ in range(31)]
max_temps = []
for i in range(len(temperatures)-6):
    segment = temperatures[i:i+7]
    max_temps.append((max(segment), i+1))
max_day = max(max_temps, key=lambda x: x[0])[1]
print(max_day)
