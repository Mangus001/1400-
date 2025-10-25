x = float(input())
y = float(input())

greater = x if x > y else y
less = x if x < y else y

print("Большее:", greater)
print("Меньшее:", less)
