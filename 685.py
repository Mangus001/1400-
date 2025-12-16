n_value = 1
while True:
    next_value = 1 + 1 / n_value
    if next_value > n_value:
        print(n_value)
        break
    n_value += 1
