s = input()
a_index = s.find('а')
o_index = s.rfind('о')
s_list = list(s)
if a_index != -1 and o_index != -1:
    s_list[a_index], s_list[o_index] = s_list[o_index], s_list[a_index]
s = ''.join(s_list)
print(s)
