n = int(input())
grades = [int(input()) for _ in range(n)]
count_fives = 0
i = 0
while i < n:
    count_fives += (grades[i] == 5)
    i += 1
