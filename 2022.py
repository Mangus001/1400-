array = [int(input()) for _ in range(int(input()))]
a = int(input())
pos = -1
for i, v in enumerate(array):
    if v < a:
        pos = i
        break
if pos == -1:
    print("Нет элементов меньше", a)
else:
    print(pos+1)
