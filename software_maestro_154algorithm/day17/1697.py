# bfs
from collections import deque

n, k = map(int, input().split())

visited = [0] * 100_001

if n < k:

    q = deque([n])
    visited[n] = 1
    while q:
        now = q.popleft()
        if now == k:
            print(visited[now] - 1)
            break

        if 0 <= now <= 100_000:
            next = [2 * now, now + 1, now - 1]
            for i in next:
                if 0 <= i <= 100_000 and not visited[i]:
                    visited[i] = visited[now] + 1
                    q.append(i)



else:
    print(n - k)

####################################################################
# dfs

import sys

sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())


# k to n
# case n < k
def dfs(k, cost):
    if n >= k:
        return cost + n - k

    if k <= 2:
        return cost + k - n

    if k % 2 == 0:
        return min(cost + k - n, dfs(k // 2, cost + 1))

    return min(dfs(k - 1, cost + 1), dfs(k + 1, cost + 1))


if n < k:
    print(dfs(k, 0))

else:
    print(n - k)
