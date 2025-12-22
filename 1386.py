def sum_of_digits(n):
    return sum(int(d) for d in str(n))

n1 = 12345
n2 = 6789
print("Сумма цифр первого числа:", sum_of_digits(n1))
print("Сумма цифр второго числа:", sum_of_digits(n2))
