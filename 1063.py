points = [ (float(input()), float(input())) for _ in range(20)]
min_x = min(p[0] for p in points)
max_x = max(p[0] for p in points)
min_y = min(p[1] for p in points)
max_y = max(p[1] for p in points)
print(f"Левый нижний: ({min_x}, {min_y})")
print(f"Правый верхний: ({max_x}, {max_y})")
