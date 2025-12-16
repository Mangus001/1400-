v = 60 
for x in range(1, v + 1):
    for y in range(1, v + 1):
        for z in range(1, v + 1):
            if x * y * z == v:
                print(x, y, z)
