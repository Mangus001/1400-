digits = list(map(int, str(n)))
k = len(digits) - 1


sum1 = 0
for i, d in enumerate(digits):
    if i % 2 == 0:
        sum1 += d
    else:
        sum1 -= d


sum2 = 0
for i, d in enumerate(digits[::-1]):
    if i % 2 == 0:
        sum2 += d
    else:
        sum2 -= d
