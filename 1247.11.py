text = input()
count_digits = sum(1 for ch in text if ch.isdigit())
print(count_digits)
