floors = [20, 15, 22, 12, 18]
min_count = min(floors)
min_floors = [i+1 for i, count in enumerate(floors) if count == min_count]
print(min_floors)
