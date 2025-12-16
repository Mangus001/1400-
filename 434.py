denominations = [64, 32, 16, 8, 4, 2, 1]
counts = {}
remaining = n
for d in denominations:
    count = remaining // d
    counts[d] = count
    remaining -= count * d
