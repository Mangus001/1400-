a = float(input())
sum_ = 2
while True:
    num = 1 + 1 / sum_
    if num >= a:
        print(num)
        sum_ += 1
    else:
        break
