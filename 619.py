b = [int(input()) for _ in range(12)]
idx = 0
found = False
for i, val in enumerate(b):
    if val % 10 == 7:
        idx = i + 1
        found = True
        break
print(found, idx if found else 0)
