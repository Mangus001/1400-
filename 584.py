a = []
while True:
    t=int(input())
    if t==-1:
        break
    a.append(t)
found=False
pos=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        found=True
        pos=i+1
        break
print(found, pos if found else 0)
