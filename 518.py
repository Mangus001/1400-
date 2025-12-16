a = [int(input()) for _ in range(20)]
sum_even_positions = sum(a[i] for i in range(1, 20, 2))
print(sum_even_positions)
