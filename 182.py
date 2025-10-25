import itertools

a, b = map(int, input("Введите размеры стола (a b): ").split())
c, d, e = map(int, input("Введите размеры костей (c d e): ").split())

sides = [
    (c, d),
    (c, e),
    (d, e)
]

max_count = 0

for side in sides:
    for orientation in [side, (side[1], side[0])]:
        width, height = orientation
        if width <= a and height <= b:
            count_horizontal = a // width
            count_vertical = b // height
            total = count_horizontal * count_vertical
            if total > max_count:
                max_count = total
        if width <= b and height <= a:
            count_horizontal = b // width
            count_vertical = a // height
            total = count_horizontal * count_vertical
            if total > max_count:
                max_count = total

print(f"Максимальное количество костей, которые можно разместить: {max_count}")
