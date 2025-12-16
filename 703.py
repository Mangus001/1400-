scores = [list(map(int, input().split())) for _ in range(8)]
max_score = max(max(row) for row in scores)
total_points = max_score
print(max_score)
print(total_points)
