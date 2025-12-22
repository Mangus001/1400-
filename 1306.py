people = [("Иванов", "женат", "есть"), ("Петров", "не женат", "нет"), ("Сидоров", "женат", "нет")]
for f, married, kids in people:
    if married == "женат" and kids == "есть":
        print(f)
