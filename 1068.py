a = [int(input()) for _ in range(10)]
b = [x*2 if x % 2 == 0 else x for x in a]
