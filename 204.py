g = int(input())
m = int(input())
n = int(input())

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def prev_day(g, m, n, leap=False):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] if leap else [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if n > 1:
        prev_n = n - 1
        prev_m = m
    else:
        prev_m = m - 1
        prev_n = days[prev_m - 1]
    return prev_m, prev_n

def next_day(g, m, n, leap=False):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] if leap else [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if n < days[m - 1]:
        next_n = n + 1
        next_m = m
    else:
        next_m = m + 1
        next_n = 1
    return next_m, next_n

leap_flag = False
pm, pn = prev_day(g, m, n, leap_flag)
nm, nn = next_day(g, m, n, leap_flag)
print(pm, pn)
print(nm, nn)

leap_flag = is_leap_year(g)
pm, pn = prev_day(g, m, n, leap_flag)
nm, nn = next_day(g, m, n, leap_flag)
print(pm, pn)
print(nm, nn)
