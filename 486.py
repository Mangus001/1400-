n = int(input())
a = list(map(float, input().split()))
print(sum(x**2 for x in a))
