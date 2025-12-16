areas_square = [float(input()) for _ in range(int(input()))]
max_area = max(areas_square)
import math
diagonals = [math.sqrt(2 * a) for a in areas_square]
max_diag = max(diagonals)
print(max_diag)
