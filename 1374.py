def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

x = float(input("Введите x: "))
y = float(input("Введите y: "))

z = sign(x) + sign(y)
print(f'z = {z}')
