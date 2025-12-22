s = input()
k = int(input())
s_num = int(input())
s_list = list(s)
s_list[k:s_num-1] = s_list[k:s_num-1][::-1]
s = ''.join(s_list)
print(s
