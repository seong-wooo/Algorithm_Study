import sys
import math

t = int(sys.stdin.readline())
ans = []
for _ in range(t):
    s_x, s_y, e_x, e_y = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    start_circle = [1 if math.sqrt((x - s_x) ** 2 + (y - s_y) ** 2) <= r else 0 for x, y, r in p]
    end_circle = [1 if math.sqrt((x - e_x) ** 2 + (y - e_y) ** 2) <= r else 0 for x, y, r in p]

    ans.append(str(sum(start_circle[i] ^ end_circle[i] for i in range(n))))

print("\n".join(ans))