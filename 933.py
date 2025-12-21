costs_candies = [random.uniform(20, 200) for _ in range(20)]
min_cost = min(costs_candies)
count_min = costs_candies.count(min_cost)
print(count_min)
