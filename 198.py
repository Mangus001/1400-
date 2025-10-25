n = int(input())

years = n // 12
months = n % 12

if 11 <= years % 100 <= 14:
    year_word = "лет"
else:
    last_digit = years % 10
    if last_digit == 1:
        year_word = "год"
    elif last_digit in [2, 3, 4]:
        year_word = "года"
    else:
        year_word = "лет"

if 11 <= months % 100 <= 14:
    month_word = "месяцев"
else:
    last_digit = months % 10
    if last_digit == 1:
        month_word = "месяц"
    elif last_digit in [2, 3, 4]:
        month_word = "месяца"
    else:
        month_word = "месяцев"

if months == 0:
    print(f"{years} {year_word} ровно")
else:
    print(f"{years} {year_word} {months} {month_word}")
