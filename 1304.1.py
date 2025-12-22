phones = [("Иванов", 89051234567), ("Петров", 8905123456), ("Сидоров", 89051234567)]
for name, phone in phones:
    if str(phone).startswith("8905"):
        print(name)
phones_str = [("Иванов", "8-905-123-45-6"), ("Петров", "8-905-123-45-7")]
for name, phone in phones_str:
    digits = ''.join(filter(str.isdigit, phone))
    if digits.startswith("8905"):
        print(name)
