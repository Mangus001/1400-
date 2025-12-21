lst = [int(input()) for _ in range(int(input()))]
first = -1
last = -1
for i, v in enumerate(lst):
    if v > 65530:
        if first == -1:
            first = i
        last = i
