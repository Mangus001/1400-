n = int(input())
total_odd = 0
total_even = 0
i = 1
while i <= n:
    residents = int(input())
    if i % 2 == 1:
        total_odd += residents
    else:
        total_even += residents
    i += 1
