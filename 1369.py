eight = 20
width = 60

for i in range(height):
    if i == 0 or i == height -1:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')
