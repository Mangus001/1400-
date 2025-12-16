n = 10  
for num in range(100, 1000):
    digits = list(map(int, str(num)))
    if sum(digits) == n:
        print(num)
