n = int(input())
d = list(map(float, input().split()))
s = float(input())
prod = 1
for num in d:
    prod *= num
print(prod > s)
