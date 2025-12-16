n = 1729 
solutions = set()
for a in range(1, 20):
    for b in range(1, a):
        sum1 = a**3 + b**3
        for c in range(1, 20):
            for d in range(1, c):
                sum2 = c**3 + d**3
                if sum1 == sum2 and sum1 == n:
                    solutions.add(tuple(sorted([a, b])))
                    solutions.add(tuple(sorted([c, d])))
print(solutions)
