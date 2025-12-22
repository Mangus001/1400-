expr = input()
parts = expr.split('+')
result = sum(int(part) for part in parts)
print(result)
