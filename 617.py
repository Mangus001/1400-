a = [float(input()) for _ in range(15)]
first_negative = 0
found = False
for i in range(15):
    if a[i] < 0:
        first_negative = i + 1
        found = True
        break
print(found, first_negative if found else 0)
