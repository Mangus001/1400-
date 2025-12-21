lst = [int(input()) for _ in range(int(input()))]
count = 0
i = 0
while i < len(lst):
    current = lst[i]
    j = i + 1
    while j < len(lst) and lst[j] == current:
        j += 1
    if j > i + 1:
        count += 1
        i = j
    else:
        i += 1
print(count)
if count > 0:
    print(*lst[j:])
