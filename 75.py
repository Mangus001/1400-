N = int(input("Введите двузначное число: "))

if N < 10 or N > 99:
    print("Ошибка: число должно быть двузначным (от 10 до 99).")
else:
  
    tens = N // 10     
    units = N % 10     
    
    sum_digits = tens + units
    
    print(f"Сумма цифр числа {N} равна {sum_digits}.")
