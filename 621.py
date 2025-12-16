sequence = [float(input()) for _ in range(20)]
count = 1
for i in range(1, 20):
    if sequence[i] == sequence[i-1]:
        count += 1
print(count)
