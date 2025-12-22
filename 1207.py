s = input()
s_list = list(s)
s_list[2:9] = s_list[2:9][::-1]
s = ''.join(s_list)
print(s
