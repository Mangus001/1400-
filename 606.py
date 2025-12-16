m = int(input())
a = list(map(int, input().split()))
filtered = [x for x in a if x % n == 0]
if filtered:
    print(sum(filtered)/len(filtered))
else:
    print(0)
