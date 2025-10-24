rice_monitor = float(input("Введите стоимость монитора: "))
price_system_block = float(input("Введите стоимость системного блока: "))
price_keyboard = float(input("Введите стоимость клавиатуры: "))
price_mouse = float(input("Введите стоимость мыши: "))

price_one_pc = price_monitor + price_system_block + price_keyboard + price_mouse

num_3 = 3
num_N = int(input("Введите количество компьютеров N: "))

cost_3 = num_3 * price_one_pc
cost_N = num_N * price_one_pc

print(f"Стоимость 3 компьютеров: {cost_3:.2f}")
print(f"Стоимость {num_N} компьютеров: {cost_N:.2f}")
