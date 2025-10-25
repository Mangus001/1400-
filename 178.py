import itertools

a = float(input("Введите сторону a кирпича: "))
b = float(input("Введите сторону b кирпича: "))
c = float(input("Введите сторону c кирпича: "))
x = float(input("Введите сторону x отверстия: "))
y = float(input("Введите сторону y отверстия: "))

edges = [a, b, c]
permutations = list(itertools.permutations(edges))

def can_pass(p):
    for (w, h) in [(x, y), (y, x)]:
        if (max(p[0], p[1]) <= w and min(p[0], p[1]) + p[2] <= h) or \
           (max(p[0], p[1]) <= h and min(p[0], p[1]) + p[2] <= w):
            return True
    return False

result = False
for p in permutations:
    if can_pass(p):
        result = True
        break

if result:
    print("Кирпич пройдет через отверстие.")
else:
    print("Кирпич не пройдет через отверстие.")
