from itertools import product

n = 20
count = 0
solutions = []

for c1 in range(n + 1):
    for c2 in range(n + 1):
        for c5 in range(n // 5 + 1):
            for t10 in range(n // 10 + 1):
                if c1 + 2 * c2 + 5 * c5 + 10 * t10 == n:
                    count += 1
                    solutions.append((c1, c2, c5, t10))
print(count)
