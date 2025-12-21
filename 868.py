def task_1150(arr):
    first_decade = sum(arr[:10]) / 10
    second_decade = sum(arr[10:20]) / 10
    third_decade = sum(arr[20:30]) / 10
    return first_decade, second_decade, third_decade
