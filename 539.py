n = int(input())
years = [int(input()) for _ in range(n)]
born_before_1990 = 0
born_after_2000 = 0
i = 0
while i < n:
    born_before_1990 += (years[i] < 1990)
    born_after_2000 += (years[i] > 2000)
    i += 1
