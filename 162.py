number = int(input())

tens = number // 10
units = number % 10

contains_4_or_7 = (tens in [4, 7]) or (units in [4, 7])

contains_3_6_9 = (tens in [3, 6, 9]) or (units in [3, 6, 9])

print("Цифры 4 или 7 входят в число:", "да" if contains_4_or_7 else "нет")
print("Цифры 3, 6 или 9 входят в число:", "да" if contains_3_6_9 else "нет")
