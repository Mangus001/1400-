rain = [float(input()) for _ in range(28)]
sum_even = 0
sum_odd = 0
i = 0
while i < 28:
    sum_even += rain[i]
    i += 2
