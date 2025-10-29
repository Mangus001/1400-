def task_5_50():
    first_day = 10
    increase = 0.10
    print("Пробег за 2-10 день:")
    for day in range(2, 11):
        distance = first_day * (1 + increase) ** (day - 1)
        print(f"День {day}: {distance:.2f} км")
    total = 0
    for day in range(1, 8):
        distance = first_day * (1 + increase) ** (day - 1)
        total += distance
    print(f"\nОбщий пробег за 7 дней: {total:.2f} км")
        
task_5_50()
