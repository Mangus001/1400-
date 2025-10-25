a3 = int(input())  
a2 = int(input())  
a1 = int(input())  
b2 = int(input())  
b1 = int(input())  

s = (100 * a3 + 10 * a2 + a1) + (10 * b2 + b1)

c3 = s // 100
c2 = (s // 10) % 10
c1 = s % 10

print(c3)
print(c2)
print(c1)
