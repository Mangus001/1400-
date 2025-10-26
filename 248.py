month_number = int(input("Введите номер месяца: "))
is_leap = input("Год високосный? (да/нет): ").lower() == "да"

days_in_month = {
    1: 31,
    2: 29 if is_leap else 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
print("Количество дней:", days_in_month.get(month_number, "Некорректный номер"))
