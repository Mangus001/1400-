a, b, k = map(int, input().split())

def divisor_count(n):
    count = 0
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

for num in range(a, b+1):
    if divisor_count(num) == k:
        print(num)
