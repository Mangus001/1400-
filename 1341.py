num1 = 584
num2 = 377

def max_digit_info(n):
    s = str(n)
    max_digit = max(s)
    index_from_start = s.index(max_digit)  # позиция с начала
    index_from_end = len(s) - 1 - s.rindex(max_digit)  # с конца
    return max_digit, index_from_start, index_from_end

max_digit1, start_pos1, end_pos1 = max_digit_info(num1)
max_digit2, start_pos2, end_pos2 = max_digit_info(num2)

same_side = (start_pos1 == start_pos2) or (end_pos1 == end_pos2)
print('Обладает ли максимальная цифра у обоих чисел одинаково расположенной стороной:', same_side)
