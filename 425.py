index_2 = number_str.find('2')
index_5 = number_str.find('5')
if index_2 != -1 and index_5 != -1:
    if index_2 < index_5:
        left_digit = '2'
    else:
        left_digit = '5'
else:
    left_digit = None
