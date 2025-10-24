N = int(input("Введите номер квартиры: "))

apartments_per_floor = 3

floors = 5

floor_number = (N - 1) // apartments_per_floor + 1

if N < 1 or N > 15:
    print("Некорректный номер квартиры.")
else:
    print(f"Квартира № {N} находится на этаже № {floor_number}")
