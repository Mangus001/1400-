models = [("Модель1", 5, 20000), ("Модель2", 7, 30000)]
avg_age = sum(price for _, age, price in models if age>6)/sum(1 for _, age, _ in models if age>6)
