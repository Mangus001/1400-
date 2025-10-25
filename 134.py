m = int(input())
n = int(input())

if n != 0:
    if m % n == 0:
        print(m // n)
    else:
        print("m на n нацело не делится")
else:
    print("деление на ноль невозможно")
