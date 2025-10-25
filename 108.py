import math

y = float(input())

angle_minutes = y

full_hours = int((y // (math.pi / 6))) 

remaining_radians = y - full_hours * (math.pi / 6)

full_minutes = int(remaining_radians // (math.pi / 30))

print("угол минутной стрелки:", angle_minutes)
print("полных часов:", full_hours)
print("полных минут:", full_minutes)
