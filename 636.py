n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
max_sum = max(a + b for a, b in pairs)
min_product = min(a * b for a, b in pairs)
print(max_sum)
print(min_product)
