for i in range(6):
    print((8, 8, 8))
for i in range(7):
    print((i+1, i+1, i+1))
for i in range(8, 81, 10):
    print((i, i, i))
for i in range(12, 83, 10):
    print((i, i, i))
for start in range(2, 21):
    print(*range(start, 21))
for start in range(15, 0, -1):
    print(*range(start, 2, -1))
for row in range(6):
    print(*([0]*6))
for row in range(5, 0, -1):
    print(*([8]*row))
for row in range(2, 11):
    print(*([row]*min(row, tenth_row)))
