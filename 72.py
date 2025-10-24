N = int(input("Введите номер квартиры: "))

total_in_entrance = 54
apartments_per_floor = 6

entrance = (N - 1) // total_in_entrance + 1

local_number = (N - 1) % total_in_entrance

floor_in_entrance = local_number // apartments_per_floor + 1

apartment_in_floor_number = (local_number % apartments_per_floor) + 1

# Вывод результатов
print(f"Квартира № {N} находится в подъезде № {entrance}")
print(f"На этаже № {floor_in_entrance} этого подъезда")
print(f"Этот этаж — {apartment_in_floor_number} по счету")
