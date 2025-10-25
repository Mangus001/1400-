n = int(input())

is_even = (n % 2 == 0)

ends_with_7 = (n % 10 == 7)

print("Четное" if is_even else "Нечетное")
print("Заканчивается на 7" if ends_with_7 else "Не заканчивается на 7")
