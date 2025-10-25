h = int(input())
m = int(input())
s = int(input())

angle_hours = (h % 12) * 30 + (m * 0.5) + (s * (0.5 / 60))

print(angle_hours)
