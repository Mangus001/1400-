scores = [int(input()) for _ in range(20)]
n = int(input())
import bisect
pos = bisect.bisect_left(scores[::-1], n)
rank = len(scores) - pos
print(rank)
