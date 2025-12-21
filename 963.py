feb_temps = [0, -2, -3, -1, -4, -2, -3, -1, -2, -3, -1, -2, -4, -1, -3, -2, -2, -3, -1, -2, -4, -1, -3, -2, -1, -2, -3, -1, -2]
cold_days = sorted(enumerate(feb_temps), key=lambda x: x[1])[:2]
print([day for day, temp in cold_days])
