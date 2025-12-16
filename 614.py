heights = list(map(float, input().split()))
min_height = heights[-1]
max_height = heights[0]
new_height = float(input())

import math
indices = [i for i, h in enumerate(heights) if min_height < h < max_height]
from bisect import bisect
position = bisect(heights, new_height)
print(position+1)
