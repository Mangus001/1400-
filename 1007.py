lst = [int(input()) for _ in range(int(input()))]
n = int(input())
index = -1
for i, val in enumerate(lst):
    if val == n:
        index = i
        break
if index == -1:
    print(*lst)
else:
    print(n, *lst[:index], *lst[index+1:])
num = int(input())
lst = [int(input()) for _ in range(int(input()))]
idx = -1
for i, val in enumerate(lst):
    if val == num:
        idx = i
        break
if idx != -1:
    print(*lst[:idx], *lst[idx+1:])
index = int(input())
num = int(input())
lst = [int(input()) for _ in range(int(input()))]
idx = -1
for i, val in enumerate(lst):
    if i == index:
        print(num, *lst[:i], *lst[i:])
        break
