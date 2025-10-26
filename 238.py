a, b = int(input()), int(input())
if a != 0 and b != 0:
    if a % b == 0:
        print("a делитель b")
    elif b % a == 0:
        print("b делитель a")
    else:
        print("ни одно из чисел не делитель другого")
