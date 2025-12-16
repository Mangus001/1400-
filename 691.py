prev_num = 2/1
prev_denom = 1
num1 = 1
denom1 = 1
while True:
    curr_num = num1 + prev_num
    curr_denom = denom1 + prev_denom
    if abs(curr_num / curr_denom - prev_num / prev_denom) <= 0.001:
        print(curr_num, '/', curr_denom)
        break
    prev_num, prev_denom = curr_num, curr_denom
    num1, denom1 = num1, denom1
