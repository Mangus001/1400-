arr = [random.randint(1,10) for _ in range(20)]
from collections import Counter
counts = Counter(arr)
only_two = list(counts.values()).count(2) == 1
print(only_two)
