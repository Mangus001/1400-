number = int(input())

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

if hundreds == units:
    print("число является палиндромом")
else:
    print("число не является палиндромом")
