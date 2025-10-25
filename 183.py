k = int(input("Введите число k (1 ≤ k ≤ 365): "))

day_of_week = (k - 1) % 7

if day_of_week in [5, 6]:
    print("Выходной день (суббота или воскресенье).")
else:
    print("Рабочий день.")
