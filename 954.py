wind_dirs = [2, 4, 6, 1, 8, 3, 5, 7]
from collections import Counter
counter = Counter(wind_dirs)
min_dir = min(counter, key=counter.get)
print(min_dir)
