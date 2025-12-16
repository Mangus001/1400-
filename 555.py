n = int(input())
precipitations = list(map(float, input().split()))
no_precip = [0 if p > 0 else 1 for p in precipitations]
cumulative = [sum(no_precip[:i+1]) for i in range(n)]
max_len = max([i for i, val in enumerate(cumulative) if val != 0]+[-1]) + 1
max_len = max_len if max_len != 0 else 0
