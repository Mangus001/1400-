for num in range(10, 100):
    last_digit = num % 10
    if last_digit in [3, 7]:
        print(num)
