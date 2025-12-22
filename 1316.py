students = [("Иванов", 12, "ул.Ленина", 15, 11), ("Петров", 11, "ул.Мира", 8, 9)]
result = []
for f, school, addr, cls, _ in students:
    if school == 15 and cls in [10,11]:
        result.append((f, addr))
for item in result:
    print(item)
