numbers = [2, 4, 6, 8]
ending_digit = '8'
results = {n: str(n).endswith(ending_digit) for n in numbers}
print(results)
