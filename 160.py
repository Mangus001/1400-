a = int(input())
b = int(input())

condition = (a != 0 and b % a == 0) or (b != 0 and a % b == 0)

print("Хотя бы одно число делитель другого:", "да" if condition else "нет")
