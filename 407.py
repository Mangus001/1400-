n = int(input())
number_str = str(n)
pos = 0
for i in range(len(number_str)-1, -1, -1):
    if number_str[i] == '3':
        pos = len(number_str) - i
        break
print(pos)
