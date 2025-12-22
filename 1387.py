def count_digits(n):
    return len(str(abs(n)))

n1 = 12345
n2 = -9876
print("Количество цифр первого числа:", count_digits(n1))
print("Количество цифр второго числа:", count_digits(n2))
