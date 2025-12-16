n = int(input())
last_index = 0
first_index = 0
for i in range(n):
    num = int(input())
    if num == 10:
        last_index = i+1
        if first_index == 0:
            first_index = i+1
print(last_index)
print(first_index)
