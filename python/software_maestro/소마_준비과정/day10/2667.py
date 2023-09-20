import sys
from collections import deque

n = int(sys.stdin.readline())
houses = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

result = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for y in range(n):
    for x in range(n):
        if houses[y][x]:
            q = deque([(y, x)])
            houses[y][x] = 0
            count = 1

            while q:
                a, b = q.popleft()
                for i in range(4):
                    na = a + dy[i]
                    nb = b + dx[i]
                    if 0 <= na < n and 0 <= nb < n and houses[na][nb]:
                        houses[na][nb] = 0
                        q.append((na, nb))
                        count += 1

            result.append(count)

print(len(result))
print("\n".join(map(str, sorted(result))))