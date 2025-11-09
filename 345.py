for num in range(100, 1000):
    square = num * num
    if str(square)[-3:] == str(num):
        print(num)
