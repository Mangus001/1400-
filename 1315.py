phonebook = [("Иванов", 89051234567), ("Петров", 8905123456)]
search_phone = 8905123456
found = False
for f, p in phonebook:
    if p == search_phone:
        print(f)
        found=True
if not found:
    print("Нет")
found_name = None
for f, p in phonebook:
    if p == search_phone:
        print(f)
        break
