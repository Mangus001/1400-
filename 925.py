arr = [random.randint(1,10) for _ in range(20)]
counts = Counter(arr)
two_elements = [k for k, v in counts.items() if v == 2]
print(two_elements)
