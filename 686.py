import math

a = float(input())
n = 0
while True:
    if n**3 - a >= 0:
        print(n)
        break
    n += 1
