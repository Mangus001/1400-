n = int(input("Введите n: "))
for num in range(1, n + 1):
    divisors = sum(1 for i in range(1, num + 1) if num % i == 0)
    print(str(num) + '+' * divisors)
