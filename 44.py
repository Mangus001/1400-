a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

sum_ab = a + b
diff_ab = a - b
prod_ab = a * b

if b != 0:
    div_ab = a / b
    print(f"Сумма: {sum_ab}")
    print(f"Разность: {diff_ab}")
    print(f"Произведение: {prod_ab}")
    print(f"Частное от деления первого числа на второе: {div_ab}")
else:
    print(f"Сумма: {sum_ab}")
    print(f"Разность: {diff_ab}")
    print(f"Произведение: {prod_ab}")
    print("Деление на ноль невозможно.")
