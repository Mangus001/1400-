count = 0
total_cost = 0
while True:
    try:
        cost = float(input())
        if cost > 1000:
            total_cost += cost
        count += 1
    except EOFError:
        break
print(total_cost)
