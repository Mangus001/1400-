a = 2
b = 2.8
step = 0.1
value = a
while value <= b + 1e-9:
    print(f"{value:.1f}")
    value += step
