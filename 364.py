n = int(input())
divisors_sum = 0
for i in range(1, n):
    if n % i == 0:
        divisors_sum += i
print("Совершенное" if divisors_sum == n else "Не совершенное")
