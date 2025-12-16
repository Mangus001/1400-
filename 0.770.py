import random

zeros = 0
ones = 0

for _ in range(50):
    num = random.randint(0, 1)
    if num == 0:
        zeros += 1
    else:
        ones += 1

print(f"Количество нулей: {zeros}")
print(f"Количество единиц: {ones}")
