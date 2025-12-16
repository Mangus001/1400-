n = int(input())
squares = [1, 4, 9, 16, 25]
for num in squares:
    if num > n:
        print(num)
        break
else:
    print("Нет таких чисел")
