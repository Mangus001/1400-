import math
n=int(input())
pair_counts=0
zero_zero=0
even=0
fives=0
for _ in range(n):
    a=int(input())
    b=int(input())
    if a==b:
        pair_counts+=1
    if a==0 and b==0:
        zero_zero+=1
    if a%2==0 and b%2==0:
        even+=1
    if a%10==5 and b%10==5:
        fives+=1
print(pair_counts, zero_zero, even, fives)
