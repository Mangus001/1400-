s = input()
indices_e = [i+1 for i, ch in enumerate(s) if ch == 'е']
if indices_e:
    print(indices_e[0])
    print(indices_e[-1])
