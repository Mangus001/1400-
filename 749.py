k = 30  
solutions = set()
for x in range(1, 31):
    for y in range(1, 31):
        if x*x + y*y == k*k:
            if x <= y:
                solutions.add((x, y))
print(solutions)
