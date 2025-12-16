a = float(input())
sum_ = 2
while True:
    num = 1 + 1 / sum_
    if num < a:
        print(num)
        break
    sum_ += 1
