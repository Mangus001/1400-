lst = [int(input()) for _ in range(int(input()))]
import itertools
indices_first = tuple(itertools.chain.from_iterable([[0], [len(lst)]]))
mods = [i for i, v in enumerate(lst) if v == 5]
first = mods[0] if mods else -1
last = mods[-1] if mods else -1
