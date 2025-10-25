k = int(input())

if 11 <= k % 100 <= 14:
    suffix = "грибов"
else:
    last_digit = k % 10
    if last_digit == 1:
        suffix = "гриб"
    elif last_digit in [2, 3, 4]:
        suffix = "гриба"
    else:
        suffix = "грибов"

print(f"Мы нашли {k} {suffix} в лесу")
