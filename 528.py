n = int(input())
m = [int(input()) for _ in range(n)]
sum_lt_25_5 = 0
sum_not_exceed_20 = 0
for x in m:
    sum_lt_25_5 += x
    sum_not_exceed_20 += x
