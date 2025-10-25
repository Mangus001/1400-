number = int(input("Введите шестизначное число: "))

if 100000 <= number <= 999999:
    d1 = number // 100000
    d2 = (number % 100000) // 10000
    d3 = (number % 10000) // 1000
    d4 = (number % 1000) // 100
    d5 = (number % 100) // 10
    d6 = number % 10

    sum_first_three = d1 + d2 + d3
    sum_last_three = d4 + d5 + d6

    if sum_first_three == sum_last_three:
        print("Число является счастливым.")
    else:
        print("Число не является счастливым.")
else:
    print("Введено не шестизначное число.")
