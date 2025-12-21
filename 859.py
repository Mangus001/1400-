def task_1141(arr, s, k):
    is_s_positive = arr[s] > 0
    is_k_even = arr[k] % 2 == 0
    larger = arr[k] if arr[k] > arr[s] else arr[s]
    return is_s_positive, is_k_even, larger
