a = list(map(float, input().split()))
total = sum(x for x in a if x > 10.75)
print(total)
