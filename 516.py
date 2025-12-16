d = [int(input()) for _ in range(10)]
total = sum(x for x in d if x % 2 == 0)
print(total)
