N = int(input("Введите номер места (от 1 до 1200): "))

if not (1 <= N <= 1200):
    print("Некорректный номер места.")
else:
    places_per_section = 150
    places_per_rack = 15

    section = (N - 1) // places_per_section + 1

    position_in_section = (N - 1) % places_per_section

    floor = position_in_section // places_per_rack + 1

    print(f"Место № {N} расположено в секции № {section}, на ярусе № {floor}.")
