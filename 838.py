arr = []
num = 300
while len(arr) < 20:
    if num % 13 == 0 or num % 17 == 0:
        arr.append(num)
    num += 1
print(arr)
