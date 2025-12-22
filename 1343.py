number = 583
digits_to_check = ['1', '4', '5', '8']
result = {d: d in str(number) for d in digits_to_check}
print(result)
