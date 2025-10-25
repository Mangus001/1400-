volume1 = float(input())
mass1 = float(input())
volume2 = float(input())
mass2 = float(input())

density1 = mass1 / volume1
density2 = mass2 / volume2

result = "первый" if density1 > density2 else "второй"

print(result)
