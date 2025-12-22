import datetime
today_month = datetime.date.today().month
today_year = datetime.date.today().year
employees = [("Иванов", "Иван", "Иваныч", "ул.Пушкина", 2010, 5),
             ("Петров", "Петр", "Петрович", "ул.Ленина", 2019, 11)]
for f, n, o, addr, y, m in employees:
    years_work = today_year - y
    if m > today_month:
        years_work -= 1
    if years_work >= 3:
        print(f, n, o, addr)
