s = input()
m = int(input())
n = int(input())
s_list = list(s)
s_list[m-1], s_list[n-1] = s_list[n-1], s_list[m-1]
s = ''.join(s_list)
print(s)
