x = int(input())
a = list(map(int, input().split()))
filtered = [num for num in a if num > x]
if filtered:
    print(sum(filtered)/len(filtered))
else:
    print(0)
