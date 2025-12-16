income = [list(map(float, input().split())) for _ in range(10)]
total_per_shop = [sum(shop) for shop in income]
max_shop = total_per_shop.index(max(total_per_shop))
max_day = max(range(10), key=lambda d: sum(income[d]))
max_value = max(max(shop) for shop in income)
max_shop_day = [(shop_idx+1, day_idx+1, income[day_idx][shop_idx]) for day_idx in range(10) for shop_idx in range(3) if income[day_idx][shop_idx] == max_value]
max_shop_idx = max_shop + 1
max_day_idx = max_day + 1
print(max_shop_idx)
print(max_day_idx)
for entry in max_shop_day:
    print(entry[0], entry[1], entry[2])
