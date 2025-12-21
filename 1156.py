sentence = input()
s_c = sentence.rfind('с')
t_c = sentence.rfind('т')
if s_c > t_c:
    print('с')
elif t_c > s_c:
    print('т')
else:
    print('равно или отсутствуют')
