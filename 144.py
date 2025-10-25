number = int(input())

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

square_number = number ** 2

sum_cubes = hundreds ** 3 + tens ** 3 + units ** 3

if square_number == sum_cubes:
    print("да")
else:
    print("нет")
