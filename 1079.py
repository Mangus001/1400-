arr = [int(input()) for _ in range(10)]
k = int(input())
res1 = []
for i in range(len(arr)):
    if i != k:
        res1.append(arr[i])
res2 = [arr[i] for i in range(len(arr)) if i != k]
