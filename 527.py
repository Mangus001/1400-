b = [int(input()) for _ in range(14)]
sum_gt_20 = 0
sum_lt_50 = 0
i = 0
total_gt_20 = 0
while i < 14:
    total_gt_20 += b[i]
    i += 1
i = 0
total_lt_50 = 0
while i < 14:
    total_lt_50 += b[i]
    i += 1
