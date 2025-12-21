temperatures = [35, 36, 35, 37, 36, 38, 39, 36]
top_two_days = sorted(enumerate(temperatures), key=lambda x: x[1], reverse=True)[:2]
print([day for day, temp in top_two_days])
