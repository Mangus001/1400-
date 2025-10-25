number = int(input())

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

if hundreds > units:
    print("Первая цифра больше последней")
elif hundreds < units:
    print("Последняя цифра больше первой")
else:
    print("Первая и последняя цифры равны")

if hundreds > tens:
    print("Первая цифра больше второй")
elif hundreds < tens:
    print("Вторая цифра больше первой")
else:
    print("Первая и вторая цифры равны")

if tens > units:
    print("Вторая цифра больше последней")
elif tens < units:
    print("Последняя цифра больше второй")
else:
    print("Вторая и последняя цифры равны")
