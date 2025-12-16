costs_set1 = list(map(float, input().split()))
costs_set2 = list(map(float, input().split()))
print("Бюджетный набор" if sum(costs_set1) < sum(costs_set2) else "Дешевле набор 2" if sum(costs_set1) > sum(costs_set2) else "Одинаковая стоимость")
