for num in range(100, 1000):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    if s == num:
        print(num)
