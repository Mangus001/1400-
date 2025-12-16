def sum_divisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

for num in range(50, 71):
    print(f"{num}: сумма делителей = {sum_divisors(num)}")
