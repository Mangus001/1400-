print("Дюймы\tСантиметры")
for inches in range(10, 23):
    cm = inches * 2.54
    print(f"{inches}\t{cm:.2f}")
