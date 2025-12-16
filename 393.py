n = int(input())
m = int(input())

digits = [int(d) for d in str(n)]
if m > len(digits):
    m = len(digits)

sum_last_m = sum(digits[-m:])
print(sum_last_m)
