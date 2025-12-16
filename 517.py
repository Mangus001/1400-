numbers = [int(input()) for _ in range(10)]
total = sum(x for x in numbers if x % 10 == 0)
print(total)
