areas = [float(input()) for _ in range(10)]
yields = [float(input()) for _ in range(10)]
total_wheat = sum(areas[i] * yields[i] for i in range(10))
avg_yield = sum(yields) / 10
print(total_wheat)
print(avg_yield)
