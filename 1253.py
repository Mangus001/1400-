number_str = input()
digits = [int(ch) for ch in number_str if ch.isdigit()]
print(sum(digits))
