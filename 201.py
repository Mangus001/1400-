birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения: "))
current_year = int(input("Текущий год: "))
current_month = int(input("Текущий месяц: "))

if current_month >= birth_month:
    age_years = current_year - birth_year
else:
    age_years = current_year - birth_year - 1

if current_month >= birth_month:
    full_months = current_month - birth_month
else:
    full_months = current_month + (12 - birth_month)

print(f"Возраст: {age_years} лет и {full_months} месяцев")
