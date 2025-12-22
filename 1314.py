from datetime import date
today_day = date.today().day
birthdays = [("Иванов", 10, 5, 2000), ("Петров", 15, 9, 2002)]
for f, d, m, y in birthdays:
    if d == today_day:
        print(f)
