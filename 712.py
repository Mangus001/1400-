costs = [float(input()) for _ in range(5)]
sales = [list(map(int, input().split())) for _ in range(5)]

income_per_type = [costs[i]*sum(sales[i]) for i in range(5)]

income_per_day = [sum(costs[i]*sales[i][j] for i in range(5)) for j in range(6)]

total_income = sum(income_per_day)

max_type_idx = income_per_type.index(max(income_per_type)) + 1

max_day_idx = income_per_day.index(max(income_per_day)) + 1

X = float(input("Введите X: "))
count_days = sum(1 for income in income_per_day if income > X)

print("Доход по видам:", income_per_type)
print("Доход по дням:", income_per_day)
print("Общий доход:", total_income)
print("Максимальный доход у вида:", max_type_idx)
print("День с максимальным доходом:", max_day_idx)
print("Количество дней, когда доход превысил X:", count_days)
