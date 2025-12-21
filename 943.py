heights = [random.uniform(150, 200) for _ in range(35)]
max_height = max(heights)
biggest_count = heights.count(max_height)
print(biggest_count)
