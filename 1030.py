growths = [int(input()) for _ in range(15)]
growths = sorted(growths, reverse=True)
new_growth = int(input())
import bisect
pos = bisect.bisect_left(growths, new_growth, hi=len(growths))
print(pos+1)  
