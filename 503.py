numbers = []
num = int(input())
while num >= 0:
    numbers.append(num)
    num = int(input())
print(sum(numbers)/len(numbers))
