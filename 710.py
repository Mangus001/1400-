income = [list(map(float, input().split())) for _ in range(10)]
max_per_shop = [max(shop) for shop in income]
max_per_day = [max(day) for day in zip(*income)]
for i, shop_max in enumerate(max_per_shop):
    print(i+1, end=' ')
print()
for i, day_max in enumerate(max_per_day):
    print(i+1, end=' ')
print()
