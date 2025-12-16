a = list(map(int, input().split()))
found=False
pos=0
for i in range(len(a)-1):
    if a[i]%2!=0 and a[i+1]%2!=0:
        found=True
        pos=i+1
        break
print(found, pos if found else 0)
