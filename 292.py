a = int(input("Введите a (a ≤ 200): "))
b = 200
count = b - a + 1
sum_numbers = sum(range(a, b + 1))
average = sum_numbers / count
print(average)
