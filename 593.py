sequence = list(map(int, input().split()))
sequence.pop()  # удаляем последнее отрицательное число
print(all(x == sequence[0] for x in sequence))
