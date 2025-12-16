n = int(input())
a = list(map(int, input().split()))
filtered = [x for x in a if x > n]
print(sum(filtered)/len(filtered))
