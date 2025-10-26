a, b, c, d = int(input()), int(input()), int(input()), int(input())
sum_div_3 = 0
if a % 3 == 0:
    sum_div_3 += a
if b % 3 == 0:
    sum_div_3 += b
if c % 3 == 0:
    sum_div_3 += c
if d % 3 == 0:
    sum_div_3 += d
print(sum_div_3)
