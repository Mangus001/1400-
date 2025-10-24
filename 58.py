num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
summa = num1 + num2
raznost = num1 - num2
proizvedenie = num1 * num2

if num2 != 0:
    chastnoe = num1 / num2
else:
    chastnoe = "Деление на ноль невозможно"

srednee = (num1 + num2) / 2

print(f"{num1}+{num2}={summa} "
      f"{num1}-{num2}={raznost} "
      f"{num1}*{num2}={proizvedenie} "
      f"{num1}/{num2}={chastnoe} "
      f"({num1}+{num2})/2={srednee}")
