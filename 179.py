import itertools

a1, a2, a3 = map(float, input("Введите размеры чемодана (a1, a2, a3): ").split())
b1, b2, b3 = map(float, input("Введите размеры коробки (b1, b2, b3): ").split())

permutations = list(itertools.permutations([b1, b2, b3]))

может_поместиться = False

for perm in permutations:
    if all(perm[i] <= [a1, a2, a3][i] for i in range(3)):
        может_поместиться = True
        break

if может_поместиться:
    print("Можно поместить коробку в чемодан. Есть возможность сэкономить на оплате.")
else:
    print("Невозможно поместить коробку в чемодан при параллельном и перпендикулярном расположении.")
