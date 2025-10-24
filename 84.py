import itertools

N = int(input("Введите трехзначное число с различными цифрами: "))

if N < 100 or N > 999:
    print("Ошибка: число должно быть трехзначным.")
else:
    hundreds = N // 100
    tens = (N // 10) % 10
    units = N % 10
    
    digits = [hundreds, tens, units]
    if len(set(digits)) != 3:
        print("Ошибка: все цифры должны быть различны.")
    else:
        permutations = set(itertools.permutations(digits))
        
        numbers = []
        for perm in permutations:
            num = perm[0]*100 + perm[1]*10 + perm[2]
            numbers.append(num)
        
        print("Образованные числа при перестановке цифр:")
        for num in sorted(numbers):
            print(num)
