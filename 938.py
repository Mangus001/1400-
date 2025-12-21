speeds = [random.uniform(30, 200) for _ in range(40)]
max_speed = max(speeds)
first_max_index = speeds.index(max_speed) + 1
last_max_index = len(speeds) - 1 - speeds[::-1].index(max_speed)
print(first_max_index, last_max_index)
