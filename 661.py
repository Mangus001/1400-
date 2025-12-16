positions = []
times = []
for _ in range(81):
    stage_time, position_type = input().split()
    stage_time = int(stage_time)
    position_type = int(position_type)
    positions.append(position_type)
    times.append(stage_time)
first_place_index = positions.index(1)
last_place_index = len(positions) - 1 - positions[::-1].index(3)
result = first_place_index < last_place_index
print("да" if result else "нет")
