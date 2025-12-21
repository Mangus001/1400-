capacities = list(map(int, input().split()))
costs = list(map(int, input().split()))
s = int(input())
for cap, cost in zip(capacities, costs):
    if cost > s:
        print(cap)
