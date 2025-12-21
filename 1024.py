array = [int(input()) for _ in range(int(input()))]
a = int(input())
pos = -1
for i, v in enumerate(array):
    if v < a:
        pos = i
        break
if pos == -1:
    print("Элементов, меньших", a, "нет")
else:
    print(*array[:pos], *array[pos:])
