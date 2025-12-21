arr = [int(input()) for _ in range(10)]
odd_same_place = [ x if x % 2 !=0 else 0 for x in arr]
odd_consecutive = [ x for x in arr if x % 2 !=0]
