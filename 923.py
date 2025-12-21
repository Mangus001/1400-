arr = [random.randint(1,10) for _ in range(20)]
has_duplicates = len(arr) != len(set(arr))
print(has_duplicates)
