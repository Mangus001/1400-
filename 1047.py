engine_powers = list(map(int, input().split()))
costs = list(map(int, input().split()))
for p, c in zip(engine_powers, costs):
    if p <= 80:
        print(c)
