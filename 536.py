n = 12
heights = [float(input()) for _ in range(n)]
count_less_165 = 0
i = 0
while i < n:
    count_less_165 += (heights[i] < 165)
    i += 1
