total_rain = 0
for day in range(1, 32):
    precip = float(input())
    if day % 2 == 0:
        total_rain += precip
print(total_rain)
