staff = [("Кузин", "ул.Ленина"), ("Иванов", "ул.Мира")]
names = ["Кузин", "Куравлев", "Кудин", "Кульков", "Кубиков"]
for f, addr in staff:
    if f in names:
        print(addr)
