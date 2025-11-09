n = int(input("Введите n: "))
for num in range(10, 100):
    str_num = str(num)
    if num % n == 0 or str(n) in str_num:
        print(num)
