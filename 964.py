results_100m = [10.23, 10.15, 10.20, 10.10, 10.25]
best_four_indices = sorted(range(len(results_100m)), key=lambda i: results_100m[i])[:4]
print(best_four_indices)
