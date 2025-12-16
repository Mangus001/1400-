index_a = number_str.rfind(a)
index_b = number_str.rfind(b)
if index_a != -1 and index_b != -1:
    if index_a > index_b:
        right_digit = a
    else:
        right_digit = b
else:
    right_digit = None
