x = list(map(int, input().split()))
print(all(x[i] == x[0] for i in range(1,12)))
