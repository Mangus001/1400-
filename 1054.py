precipitations = list(map(float, input().split()))
temperatures = list(map(float, input().split()))
snow = 0
rain = 0
for p, t in zip(precipitations, temperatures):
    if t > 0:
        rain += p
    else:
        snow += p
print('Осадков в виде снега:', snow)
print('Осадков в виде дождя:', rain)
