nums = [int(input()) for _ in range(14)]
evens = [num for num in nums if num % 2 == 0]
max_even = max(evens) if evens else None
print(max_even)
