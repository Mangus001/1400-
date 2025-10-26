b = int(input("Введите b (b ≥ 150): "))
a = 150
count = b - a + 1
sum_numbers = sum(range(a, b + 1))
average = sum_numbers / count
print(average)
