number = int(input())

last_digit = number % 10

ends_with_even = (last_digit % 2 == 0)

ends_with_odd = (last_digit % 2 != 0)

print("Заканчивается четной цифрой:", "да" if ends_with_even else "нет")
print("Заканчивается нечетной цифрой:", "да" if ends_with_odd else "нет")
