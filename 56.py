X = float(input("Введите температуру в градусах Цельсия: "))

fahrenheit = X * 1.8 + 32
kelvin = X + 273.15

print(f"Температура по шкале Фаренгейта: {fahrenheit:.2f}")
print(f"Температура по шкале Кельвина: {kelvin:.2f}")
