n = int(input())

if 11 <= n % 100 <= 14:
    word = "лет"
elif n % 10 == 1:
    word = "год"
elif n % 10 in [2, 3, 4]:
    word = "года"
else:
    word = "лет"

print(f"Мне {n} {word}")
