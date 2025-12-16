def min_bills(amount):
    counts = {}
    denominations = [64, 32, 16, 8, 4, 2, 1]
    remaining = amount
    for d in denominations:
        c = remaining // d
        counts[d] = c
        remaining -= c * d
    return counts

n = int(input())
for val in range(n, n + 11):
    print(f'Sum: {val}')
    print(min_bills(val))
