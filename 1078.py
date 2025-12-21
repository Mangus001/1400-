arr = [float(input()) for _ in range(10)]
negatives = []
for num in arr:
    if num <0:
        negatives.append(num)
negatives_gen = [num for num in arr if num < 0]
