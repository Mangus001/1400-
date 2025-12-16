b = list(map(float, input().split()))
filtered = [x for x in b if x > 10]
if filtered:
    print(sum(filtered)/len(filtered))
else:
    print(0)
