initial = 1000
monthly_increase_percent = 2
threshold = 30
amount = initial
month = 0

while True:
    increment = amount * monthly_increase_percent / 100
    if increment > threshold:
        break
    amount += increment
    month += 1

print("Месяц, когда прирост превысит 30 руб.:", month)
