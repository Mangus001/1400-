sequence = list(map(float, input().split()))
m = float(input())
for num in sequence:
    if num < m:
        print(num)
