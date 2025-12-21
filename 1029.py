arr = [int(input()) for _ in range(22)]
valid_a = all((num % 10) == (num // 10) for num in arr)
valid_b = all((abs(num // 10 - num % 10) <= 1) for num in arr)
print("Соответствует" if valid_a and valid_b else
