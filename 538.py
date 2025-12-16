n = int(input())
grades = [int(input()) for _ in range(n)]
fives = 0
twos = 0
i = 0
while i < n:
    if grades[i] == 5:
        fives += 1
    if grades[i] == 2:
        twos += 1
    i += 1
