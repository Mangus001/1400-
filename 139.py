number = int(input())

first_digit = number // 10
second_digit = number % 10

square_number = number ** 2

sum_cubes = (first_digit ** 3) + (second_digit ** 3)
quadrupled_sum = 4 * sum_cubes

if square_number == quadrupled_sum:
    print("да")
else:
    print("нет")
