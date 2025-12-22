text = input()
digits = [int(ch) for ch in text if ch.isdigit()]
suma = sum(digits)
max_digit = max(digits) if digits else None
print(suma)
print(max_digit)
