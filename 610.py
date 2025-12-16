n = int(input())
last_pos = 0
for i in range(n):
    num = int(input())
    if num > 100:
        last_pos = i+1
print(last_pos)
