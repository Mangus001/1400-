month_number = int(input("Введите номер месяца: "))

if month_number in [12, 1, 2]:
    season = "зима"
elif month_number in [3, 4, 5]:
    season = "весна"
elif month_number in [6, 7, 8]:
    season = "лето"
elif month_number in [9, 10, 11]:
    season = "осень"
else:
    season = "Некорректный номер месяца"

print(season)
