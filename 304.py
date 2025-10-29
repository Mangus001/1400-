def task_5_42(n=100):
    position = 0
    total_distance = 0
    direction = 1 
    for k in range(1, n + 1):
        step = 1 / k
        total_distance += step
        position += direction * step
        direction *= -1
    return position, total_distance

pos, dist = task_5_42()
print(f"Расстояние от дома после 100-го этапа: {pos}")
print(f"Общий пройденный путь: {dist}")
