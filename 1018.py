lst = [int(input()) for _ in range(int(input()))]
first_odd = -1
for i, v in enumerate(lst):
    if v % 2 != 0:
        first_odd = i
        break
if first_odd == -1:
    print("Нет нечетных элементов")
else:
    print(first_odd+1)
first_13 = -1
for i, v in enumerate(lst):
    if v % 13 == 0:
        first_13 = i
        break
if first_13 == -1:
    print("Нет элементов, кратных 13")
else:
    print(first_13+1)
