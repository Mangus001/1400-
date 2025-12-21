cost_candies = [random.uniform(10, 100) for _ in range(30)]
min_cost_candy = min(cost_candies)
first_min_idx = cost_candies.index(min_cost_candy) + 1
last_min_idx = len(cost_candies) - 1 - cost_candies[::-1].index(min_cost_candy)
print(first_min_idx, last_min_idx)
