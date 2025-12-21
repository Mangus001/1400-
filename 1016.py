grades = [int(input()) for _ in range(24)]
count5 = 0
i = 0
while i < len(grades) and grades[i] == 5:
    count5 += 1
    i += 1
print(count5)
