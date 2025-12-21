import random
array = [random.randint(1, 100) for _ in range(20)]  
duplicates = set()
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] == array[j]:
            duplicates.add(array[i])
            duplicates.add(array[j])
print(list(duplicates))
