sequence = [float(input()) for _ in range(30)]
count = 1
for i in range(1, 30):
    if sequence[i] != sequence[i-1]:
        count += 1
print(count)
