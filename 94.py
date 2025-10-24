n = int(input("Введите n (от 1 до 999): "))

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if 100*b + 10*c + a == n:
                # Нашли искомое a, b, c
                x = 100*a + 10*b + c
                print(f"Найденное число x: {x}")
                break
        else:
            continue
        break
    else:
        continue
    break
