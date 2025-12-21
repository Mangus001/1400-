array = sorted([int(input()) for _ in range(30)])
if array[-1] != max(array):
    array[-1] = max(array)
