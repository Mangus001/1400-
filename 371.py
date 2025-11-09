target = 
n = 1
fact = 1
while fact < target:
    n += 1
    fact *= n
if fact == target:
    print(n)
else:
    print("Факториал не найден.")
