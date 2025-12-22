s = input()
half = len(s) // 2
s_list = list(s)
for i in range(half):
    s_list[i], s_list[-i-1] = s_list[-i-1], s_list[i]
s = ''.join(s_list)
print(s)
