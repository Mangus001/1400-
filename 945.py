costs_books = [random.uniform(100, 1000) for _ in range(60)]
min_cost_book = min(costs_books)
count_min_books = sum(1 for c in costs_books if c == min_cost_book)
print(count_min_books)
