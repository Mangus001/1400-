areas = list(map(int, input().split()))
harvests = list(map(int, input().split()))
sum_yield = 0
sum_area = 0
for area, yield_ in zip(areas, harvests):
    sum_area += area
    sum_yield += yield_
    print((yield_ / area) if area != 0 else 0)
print(sum_yield / sum(areas)
