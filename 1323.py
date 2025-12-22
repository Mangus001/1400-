cars = [("Модель1", 20000, "легковой"), ("Модель2", 30000, "грузовой")]
avg_price = sum(price for f, price, t in cars if t=="легковой")/sum(1 for f, price, t in cars if t=="легковой")
