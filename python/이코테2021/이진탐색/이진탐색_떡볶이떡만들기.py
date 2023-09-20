import sys
from bisect import bisect_right
n, m = map(int, sys.stdin.readline().split())

rc = list(map(int, sys.stdin.readline().split()))

rc.sort()

start_h = 0
end_h = max(rc)

while start_h <= end_h:
  mid_h = (start_h + end_h) // 2
  result = 0
  index = bisect_right(rc, mid_h)

  for i in range(index, n):
      result += rc[i]-mid_h
  if result == m:
    h = mid_h
    break
  elif result > m:
    start_h = mid_h + 1 
    h = mid_h
  else:
    end_h = mid_h - 1

print(h)