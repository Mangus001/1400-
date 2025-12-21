classes = [random.randint(20, 45) for _ in range(40)]
max_class = max(classes)
min_class = min(classes)
print(max_class - min_class >= 10)
