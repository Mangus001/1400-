def sum_divs(n):
    total = 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

a, b = 1, 100  
max_sum = 0
number_with_max_sum = a
for num in range(a, b + 1):
    s = sum_divs(num)
    if s > max_sum:
        max_sum = s
        number_with_max_sum = num
print(number_with_max_sum)
