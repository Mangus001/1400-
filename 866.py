def task_1148(arr):
    first_decade = sum(arr[:10])
    second_decade = sum(arr[10:20])
    third_decade = sum(arr[20:30])
    return first_decade, second_decade, third_decade
