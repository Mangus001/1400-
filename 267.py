kurs = float(input("Введите курс доллара в рубли: "))
print("Доллары\tРубли")
for dollars in range(1, 21):
    print(f"{dollars}\t{dollars * kurs:.2f}")
