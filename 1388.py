def sum_digits(number):
    return sum(int(d) for d in str(number))

count_happy = 0
for num in range(100000, 1000000):
    s1 = sum_digits(str(num)[:3])
    s2 = sum_digits(str(num)[3:])
    if s1 == s2:
        count_happy += 1
print("Количество счастливых чисел:", count_happy)
