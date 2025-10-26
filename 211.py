n = int(input())
a = int(input())

total_sum = 0
for i in range(n):
    total_sum += a + i

if total_sum % 2 == 0:
    print("Да")
else:
    print("Нет")
