heights = list(map(float, input().split()))
is_descending = all(heights[i] >= heights[i+1] for i in range(len(heights)-1))
print(is_descending)
