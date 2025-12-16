lengths = list(map(float, input().split()))
times = list(map(float, input().split()))
max_speed = -1
max_idx = -1
for i in range(25):
    speed = lengths[i] / times[i]
    if speed > max_speed:
        max_speed = speed
        max_idx = i
print(max_idx + 1)
