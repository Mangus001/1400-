a = int(input("Введите a: "))
b = int(input("Введите b (b ≥ a): "))
count = b - a + 1
sum_numbers = sum(range(a, b + 1))
average = sum_numbers / count
print(average)
