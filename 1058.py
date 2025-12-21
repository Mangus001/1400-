income_shop1 = [float(input()) for _ in range(28)]
income_shop2 = [float(input()) for _ in range(28)]
total_shop1 = sum(income_shop1)
total_shop2 = sum(income_shop2)
print("Меньше доход в первом магазине" if total_shop1 < total_shop2 else "Меньше доход во втором магазине")
