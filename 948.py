import numpy as np
arr = np.random.uniform(1, 100, 20)
max_elem = np.max(arr)
min_elem = np.min(arr)
print(max_elem - min_elem <= 25, min_elem * 2 > max_elem)
