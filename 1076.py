a = [int(input()) for _ in range(10)]
b = [1 if (a[i]>0) == (a[j]>0) else 0 for i in range(10) for j in range(10) if i==j]
