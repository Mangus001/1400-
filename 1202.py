s = input()
s_list = list(s)
s_list[2], s_list[-1] = s_list[-1], s_list[2]
s = ''.join(s_list)
print(s)
