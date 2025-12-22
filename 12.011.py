s = input()
s_list = list(s)
s_list[1], s_list[4] = s_list[4], s_list[1]
s = ''.join(s_list)
print(s)
