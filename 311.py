def task_5_49():
    initial = 1000
    growth_rate = 0.02
    print("Прирост за первые 10 месяцев:")
    for month in range(1, 11):
        previous = initial * (1 + growth_rate) ** (month - 1)
        current = initial * (1 + growth_rate) ** month
        increase = current - previous
        print(f"Месяц {month}: прирост = {increase:.2f} руб")
    print("\nСумма через 3-12 месяцев:")
    for month in range(3, 13):
        amount = initial * (1 + growth_rate) ** month
        print(f"Месяц {month}: {amount:.2f} руб")
        
task_5_49()
