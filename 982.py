heights = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60]
pos1, pos2 = 3, 7
for pos in sorted([pos1, pos2], reverse=True):
    del heights[pos - 1]
drop1, drop2 = 180, 130
heights = [h for h in heights if h != drop1 and h != drop2]
