cost_per_kg = float(input("Введите стоимость 1 кг конфет: "))
print("Вес (г)\tСтоимость")
for weight in range(100, 2100, 100):
    cost = (weight / 1000) * cost_per_kg
    print(f"{weight}\t{cost:.2f}")
