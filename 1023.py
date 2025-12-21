array = [int(input()) for _ in range(int(input()))]
n = int(input())
pos = -1
for i, v in enumerate(array):
    if v > n:
        pos = i
        break
if pos == -1:
    print("Нет элементов больше", n)
else:
    print(*array[pos:])
