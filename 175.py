a = float(input("Введите внутреннюю длину конверта (a мм): "))
b = float(input("Введите внутреннюю ширину конверта (b мм): "))
c = float(input("Введите длину открытки (c мм): "))
d = float(input("Введите ширину открытки (d мм): "))

c_with_margin = c + 2
d_with_margin = d + 2

if (c_with_margin <= a and d_with_margin <= b) or (d_with_margin <= a and c_with_margin <= b):
    print("Открытка войдет в конверт.")
else:
    print("Открытка не войдет в конверт.")
