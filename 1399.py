def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

def previous_day(year, month, day):
    if day > 1:
        return year, month, day - 1
    else:
        if month == 1:
            prev_month = 12
            prev_year = year - 1
        else:
            prev_month = month - 1
            prev_year = year
        prev_day = days_in_month(prev_year, prev_month)
        return prev_year, prev_month, prev_day

def next_day(year, month, day):
    dim = days_in_month(year, month)
    if day < dim:
        return year, month, day + 1
    else:
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        return next_year, next_month, 1

g, m, n = 2023, 3, 1
prev = previous_day(g, m, n)
next_ = next_day(g, m, n)
print(f"Предыдущий день: {prev}")
print(f"Следующий день: {next_}")
