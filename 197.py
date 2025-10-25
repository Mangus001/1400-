n = int(input())

rub = n // 100
kop = n % 100

if 11 <= rub % 100 <= 14:
    rub_word = "рублей"
else:
    last_digit = rub % 10
    if last_digit == 1:
        rub_word = "рубль"
    elif last_digit in [2, 3, 4]:
        rub_word = "рубля"
    else:
        rub_word = "рублей"

if 11 <= kop % 100 <= 14:
    kop_word = "копеек"
else:
    last_digit = kop % 10
    if last_digit == 1:
        kop_word = "копейка"
    elif last_digit in [2, 3, 4]:
        kop_word = "копейки"
    else:
        kop_word = "копеек"

if kop == 0:
    print(f"{rub} {rub_word} ровно")
else:
    print(f"{rub} {rub_word} {kop} {kop_word}")
