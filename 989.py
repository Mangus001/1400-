heights = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60]
pos1, pos2 = 4, 10
heights = heights[:pos1-1] + [185] + heights[pos1:pos2-1] + [180] + heights[pos2:]
new_height1, new_height2 = 185, 180
heights.append(new_height1)
heights.append(new_height2)
heights.sort(reverse=True)
