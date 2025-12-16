import sys
numbers = list(map(float, input().split()))
avg = sum(c for c in numbers if c > 20) / sum(1 for c in numbers if c > 20)
print(avg)
