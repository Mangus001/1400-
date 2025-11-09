s = 
count = 0
for num in range(100, 1000):
    if sum(int(digit) for digit in str(num)) == s:
        count += 1
print(count)
