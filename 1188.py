s = input()
index_n = s.find('н')
index_k = s.find('к')
if index_n != -1 and index_k != -1:
    print('н' if index_n < index_k else 'к')
