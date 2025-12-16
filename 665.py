peeds = list(map(float, input().split()))
max_speed = max(speeds)
greater_than_max = [s for s in speeds if s > max_speed]
print(max(speeds))
