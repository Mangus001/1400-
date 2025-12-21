def task1178(arr):
    even_count = sum(1 for x in arr if x % 2 == 0)
    ending_five = sum(1 for x in arr if abs(x) % 10 == 5)
    return even_count, ending_five
