m = int(input())
n = int(input())

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n > 1:
    prev_day = n - 1
    prev_month = m
else:
    prev_month = m - 1
    prev_day = month_days[prev_month - 1]

if n < month_days[m - 1]:
    next_day = n + 1
    next_month = m
else:
    next_month = m + 1
    next_day = 1

print(prev_month, prev_day)
print(next_month, next_day)
