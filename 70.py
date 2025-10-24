N = int(input("Введите номер квартиры (1–20): "))

if N < 1 or N > 20:
    print("Некорректный номер квартиры")
else:
    flats_per_floor = 4
    
    floor = (N - 1) // flats_per_floor + 1
    
    position_number = N
    
    print(f"Квартира № {N} находится на этаже № {floor}")
    print(f"Это квартира по счету: {position_number}")
