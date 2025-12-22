magazines = [(15000, 12), (8000, 8), (12000, 15)]
avg_price = sum(price for price, tir in magazines if tir<10000)/sum(1 for price, tir in magazines if tir<10000)
