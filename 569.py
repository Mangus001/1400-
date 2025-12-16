numbers = list(map(int, input().split()))
print(any(x % 2 == 0 for x in numbers))
