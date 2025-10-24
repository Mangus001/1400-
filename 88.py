#a
n = int(input("Введите число больше 99: "))
if n <= 99:
    print("Ошибка: число должно быть больше 99.")
else:
    tens = (n // 10) % 10
    print("Число десятков:", tens)
  #b
  hundreds = (n // 100) % 10
print("Число сотен:", hundreds)
