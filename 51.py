cost_candies = float(input("Введите стоимость 1 кг конфет: "))
cost_biscuits = float(input("Введите стоимость 1 кг печенья: "))
cost_apples = float(input("Введите стоимость 1 кг яблок: "))

x = float(input("Килограммов конфет куплено: "))
y = float(input("Килограммов печенья куплено: "))
z = float(input("Килограммов яблок куплено: "))

total_cost = (cost_candies * x) + (cost_biscuits * y) + (cost_apples * z)

print(f"Общая стоимость покупки: {total_cost:.2f}")
