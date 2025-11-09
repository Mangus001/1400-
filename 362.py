d = 
count_gt_d = 0
for i in range(1, n + 1):
    if n % i == 0 and i > d:
        count_gt_d += 1
print(count_gt_d)
