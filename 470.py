R_list = list(map(float, input().split()))
R_inv_sum = sum(1 / R for R in R_list)
R_total = 1 / R_inv_sum
print(R_total)
