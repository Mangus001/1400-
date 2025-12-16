points = list(map(int, input().split()))
sorted_points = sorted(points, reverse=True)
print(sum(sorted_points[:3]))
