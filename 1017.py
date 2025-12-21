lst = [int(input()) for _ in range(int(input()))]
n = int(input())
pos_first_n = -1
for i, v in enumerate(lst):
    if v == n:
        pos_first_n = i
        break
if pos_first_n != -1:
    print(*lst[:pos_first_n])
else:
    print(*lst)
pos_last_7 = -1
for i in range(len(lst)-1, -1, -1):
    if lst[i] % 10 == 7:
        pos_last_7 = i
        break
if pos_last_7 != -1:
    print(*lst[pos_last_7+1:])
