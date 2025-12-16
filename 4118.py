n = int(input())
s = [int(d) for d in str(n)]
sum_digits = sum(s)
prod_digits = 1
for d in s:
    prod_digits *= d
length = len(s)
first_digit = s[0]
last_digit = s[-1]
print(sum_digits > 10)
print(prod_digits < 50)
print(length % 2 == 0)
print(1000 <= n <= 9999)
print(first_digit <= 6)
print(s[0] == s[-1])
print("Первая больше последней:" if s[0] > s[-1] else "Последняя больше первой:")
