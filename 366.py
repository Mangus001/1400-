a = int(input())
b = int(input(()
count = 0
temp = a
while temp >= b:
    temp -= b
    count += 1
print("Целая часть:", count)
print("Остаток:", temp)
