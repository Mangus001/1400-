s = input()
s_list = list(s)
s_list[s-1], s_list[k-1] = s_list[k-1], s_list[s-1]
s_list[s-1], s_list[k-1] = s_list[k-1], s_list[s-1]
s = ''.join(s_list)
print(s)
