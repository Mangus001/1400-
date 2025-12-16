a = int(input())
b = int(input())
m = int(input())
n = int(input())
number = int(input())
s = [int(d) for d in str(number)]
sum_digits = sum(s)
prod_digits = 1
for d in s:
    prod_digits *= d
length = len(s)
first_digit = s[0]
last_digit = s[-1]
print(sum_digits < a)
print(prod_digits > b)
print(length >= 1)
print(first_digit > m)
