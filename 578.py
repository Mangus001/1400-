n=int(input())
days=0
for _ in range(n):
    precip=int(input())
    if precip==0:
        days+=1
print(days==10)
