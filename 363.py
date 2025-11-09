n = int(input())
if n > 1:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Простое" if is_prime else "Не является простым")
else:
    print("Число должно быть больше 1")
