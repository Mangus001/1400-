N = int(input("Введите трехзначное число: "))

if N < 100 or N > 999:
    print("Ошибка: число должно быть трехзначным.")
else:
    hundreds = N // 100
    tens = (N // 10) % 10
    units = N % 10
    
    sum_digits = hundreds + tens + units
    product_digits = hundreds * tens * units
    
    print(f"Число единиц: {units}")
    print(f"Число десятков: {tens}")
    print(f"Сумма цифр: {sum_digits}")
    print(f"Произведение цифр: {product_digits}")
