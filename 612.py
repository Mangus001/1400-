m = int(input())
last_neg = 0
for i in range(m):
    num = int(input())
    if num < 0:
        last_neg = i+1
print(last_neg)
