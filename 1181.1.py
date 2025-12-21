s = input()
comma_index = s.find(',')
if comma_index != -1:
    part = s[:comma_index]
    count_n = part.count('н')
    print(count_n)
else:
    print(s.count('н'))
