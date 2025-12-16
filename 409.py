n = int(input())
s = str(n)
first_digit = s[0]
count = 0
for digit in s:
    if digit == first_digit:
        count += 1
print(count)
