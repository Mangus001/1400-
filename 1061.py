lengths = [float(input()) for _ in range(25)]
times = [float(input()) for _ in range(25)]
min_avg_speed = float('inf')
for i in range(25):
    avg_speed = lengths[i] / times[i]
    if avg_speed < min_avg_speed:
        min_avg_speed = avg_speed
print("Минимальная средняя скорость", min_avg_speed)

avg_speeds = [lengths[i] / times[i] for i in range(25)]
print("Минимальная средняя скорость", min(avg_speeds))
