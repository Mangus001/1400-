start = 3.2
end = 3.9
step = 0.1
value = start
while value <= end + 1e-9:
    print(f"{value:.1f}")
    value += step
