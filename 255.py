m, n = map(int, input("Введите месяц и число: ").split())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n > 1:
    prev_day = n - 1
    prev_month = m
else:
    prev_month = m - 1
    if prev_month < 1:
        print("Это 1 января, предыдущий день отсутствует")
        prev_day = None
        prev_month = None
    else:
        prev_day = days_in_month[prev_month - 1]

if n < days_in_month[m - 1]:
    next_day = n +
