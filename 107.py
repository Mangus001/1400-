y = float(input())

full_hours = int(y // 30)

remaining_degrees = y - full_hours * 30

full_minutes = int(remaining_degrees // 0.5)

print(full_hours, full_minutes)
