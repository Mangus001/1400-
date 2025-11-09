for num in range(10, 100):
    digits = [int(d) for d in str(num)]
    s = sum(digits)
    if s + s ** 2 == num:
        print(num)
