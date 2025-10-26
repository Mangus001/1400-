cost_per_kg = float(input("Введите стоимость 1 кг сыра: "))
print("Вес (г)\tСтоимость")
for weight in range(50, 1050, 50):
    cost = (weight / 1000) * cost_per_kg
    print(f"{weight}\t{cost:.2f}")
