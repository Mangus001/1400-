counts = {i:0 for i in range(1,7)}
for _ in range(100):
    roll = random.randint(1,6)
    counts[roll] += 1
for _ in range(900):
