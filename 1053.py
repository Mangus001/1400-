engine_powers = list(map(int, input().split()))
costs = list(map(int, input().split()))
total_cost = sum(c for p, c in zip(engine_powers, costs) if p > 100)
print(total_cost)
