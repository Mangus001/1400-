count_0 = number_str.count('0')
count_9 = number_str.count('9')
if count_0 > count_9:
    result = '0'
elif count_9 > count_0:
    result = '9'
else:
    result = 'равны'
