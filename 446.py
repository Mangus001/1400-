for num in range(100, 1000):
    if num % 7 == 0:
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum % 7 == 0:
            print(num)
