n = int(input())
b = list(map(int, input().split()))
filtered = [x for x in b if x % n == 0]
print(sum(filtered)/len(filtered))
