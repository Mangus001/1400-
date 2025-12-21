sales_july = list(map(int, input().split()))
sales_aug = list(map(int, input().split()))
total = sum(sales_july) + sum(sales_aug)
print(total)
