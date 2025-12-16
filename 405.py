num = int(input())
digits = [int(d) for d in str(num)]
count_3 = digits.count(3)
count_last_digit = digits.count(digits[-1])
even_digits = [d for d in digits if d % 2 == 0]
count_even = len(even_digits)
sum_greater_5 = sum([d for d in digits if d > 5])
prod_greater_7 = 1
count_zero_fives = 0

for d in digits:
    if d > 7:
        prod_greater_7 *= d
    if d == 0 or d == 5:
        count_zero_fives += 1
