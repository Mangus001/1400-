n = 50
m = 10
def sum_digits_sq(num):
    s = 0
    while num:
        d = num % 10
        s += d * d
        num //=10
    return s
for num in range(1, n):
    if sum_digits_sq(num) == m:
        print(num)
