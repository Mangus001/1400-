a = int(input())
b = int(input())

result = 1 if (a % b == 0 or b % a == 0) else 42  # любое число кроме 1
print(result)
