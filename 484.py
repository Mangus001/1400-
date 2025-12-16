a_list = []
a = int(input())
while a != 0:
    a_list.append(a)
    a = int(input())
product = 1
for num in a_list:
    print(num, end=' ')
    product *= num
    print(product)
print(0)
