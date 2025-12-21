def task_1157(arr):
    half = len(arr) // 2
    first_half = sum(arr[:half])
    second_half = sum(arr[half:])
    max_decade = max(sum(arr[i:i+10]) for i in range(0, len(arr), 10))
    return 'first' if first_half > second_half else 'second', max_decade
