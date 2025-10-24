N = int(input("Введите трехзначное число: "))

if N < 100 or N > 999:
    print("Ошибка: число должно быть трехзначным.")
else:
    hundreds = N // 100
    tens = (N // 10) % 10
    units = N % 10
    
    print(f"{hundreds}, {tens}, {units}")
