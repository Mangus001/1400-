weight = float(input())
if weight <= 60:
    category = "легкий вес"
elif weight <= 64:
    category = "первый полусредний вес"
elif weight <= 69:
    category = "полусредний вес"
else:
    category = "выше категории"
print(category)
