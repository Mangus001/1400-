a = [int(x) for x in input().split()]
import itertools
grouped = [list(group) for _, group in itertools.groupby(a)]
last_group = len(grouped) - 1
count = len(grouped[-1]) if grouped else 0
res = []
for i in range(len(grouped) - 1):
    if len(grouped[i]) == len(grouped[i+1]) == count:
        res.extend(grouped[i])
if len(grouped) == 0:
    print(0)
    print()
elif len(grouped) == 1:
    print(count)
    print()
else:
    print(count)
    index = 0
    for g in grouped:
        if len(g) == count:
            index = grouped.index(g)
            break
    elements_after_last = grouped[index][-1]
    print(elements_after_last)
