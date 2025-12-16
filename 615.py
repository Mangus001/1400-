scores = [int(input()) for _ in range(20)]
N = int(input())
positions = list(range(1, 21))
import bisect
pos = bisect.bisect_left(scores[::-1], N)
print(pos + 1)
