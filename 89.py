
n = int(input("Введите число больше 999: "))
if n <= 999:
    print("Ошибка: число должно быть больше 999.")
else:
    hundreds = (n // 100) % 10
    print("Число сотен:", hundreds)
  thousands = (n // 1000) % 10
print("Число тысяч:", thousands)
