area = 100
yield_per_hectare = 20
year = 0
total_harvest = 0

while yield_per_hectare <= 22:
    year += 1
    area *= 1.05
    yield_per_hectare *= 1.02
    total_harvest += yield_per_hectare * area
    if total_harvest > 800:
        break
print("Год, когда урожай превысит 800 ц:", year)
