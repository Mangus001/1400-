N = int(input("Введите двузначное число: "))

if N < 10 or N > 99:
    print("Число должно быть двузначным.")
else:
    tens = N // 10
    units = N % 10
    print(f"Число десятков: {tens}")
    print(f"Число единиц: {units}")
