lst = [int(input()) for _ in range(int(input()))]
if len(lst) > 0:
    last = lst[-1]
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = last
