def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

for num in range(120, 141):
    print(f"{num} делителей: {count_divisors(num)}")
