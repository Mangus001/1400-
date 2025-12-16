c = [float(input()) for _ in range(15)]
total = 0
for i in range(0, 15, 2):
    total -= c[i]
print(total)
