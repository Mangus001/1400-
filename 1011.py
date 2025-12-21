lst = [int(input()) for _ in range(int(input()))]
indices_zero = [i for i, v in enumerate(lst) if v == 0]
if len(indices_zero) > 0:
    print(*[lst[i] for i in range(indices_zero[0]+1, len(lst))])
    print(*[lst[i] for i in range(0, indices_zero[-1])])
