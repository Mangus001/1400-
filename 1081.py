words = [input() for _ in range(20)]
import statistics
avg_length = sum(len(w) for w in words)/len(words)
count_more5 = sum(1 for w in words if len(w) > 5)
max_length = max(len(w) for w in words)
shortest_idx = next(i for i,w in enumerate(words) if len(w) == min(len(w) for w in words))
count_bigger_max = sum(1 for w in words if len(w) > max_length)
count_k = sum(1 for w in words if w.lower().startswith('к'))
sorted_words = sorted(words
