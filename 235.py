points = int(input())
if points == 3:
    result = "выигрыш"
elif points == 0:
    result = "проигрыш"
elif points == 1:
    result = "ничья"
else:
    result = "неизвестно"
print(result)
