def task1167(arr):
    odd_side = sum(arr[i] for i in range(0, len(arr), 2))
    even_side = sum(arr[i] for i in range(1, len(arr), 2))
    return 'нечёт' if odd_side > even_side else 'чёт'
