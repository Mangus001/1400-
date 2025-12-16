n=int(input())
counter=0
for _ in range(n):
    a,b,c=map(int,input().split())
    if a+b>c and a+c>b and b+c>a:
        counter+=1
print(counter)
