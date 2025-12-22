def compare_prices(price1, price2):
    total1 = price1[0]*100 + price1[1]
    total2 = price2[0]*100 + price2[1]
    if total1 > total2:
        return "Первый дороже"
    elif total1 < total2:
        return "Второй дороже"
    else:
        return "Они равны"
# пример
print(compare_prices((10,50), (10,75)))
