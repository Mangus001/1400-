import sys
count=0
prev=0
sign=None
for _ in range(int(input())):
    x=int(input())
    if _==0:
        prev=x
        continue
    current_sign = 1 if x>0 else -1
    if sign is not None and current_sign != sign:
        count+=1
    sign=current_sign
    prev=x
print(count)
