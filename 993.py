heights = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60]
pos1, pos2 = 3, 6
for pos in sorted([pos1, pos2], reverse=True):
    del heights[pos - 1]
heights.extend([175, 165]) 
heights.sort(reverse=True)
new_heights = [175, 165]
for nh in new_heights:
    index = 0
    while index < len(heights) and heights[index] >= nh:
        index += 1
    heights.insert(index, nh)
