import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

origin = "123456780"
puzzle = ""
for _ in range(3):
    puzzle += "".join(sys.stdin.readline().split())

# y, x 는 0의 위치
q = deque()
visited = {}
q.append(origin)
visited[origin] = (0, 8)  # 이동 횟수, 위치
count = 0

next_index = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [2, 4, 8],
    [3, 7],
    [4, 6, 8],
    [5, 7]
]
while q:
    origin = q.popleft()

    if origin == puzzle:
        print(visited[origin][0])
        break

    count, index = visited[origin]

    dindex = next_index[index]

    li_origin = list(origin)
    for d in dindex:
        li_origin[index], li_origin[d] = li_origin[d], li_origin[index]
        c_origin = "".join(li_origin)
        if c_origin not in visited:
            visited[c_origin] = (count + 1, d)
            q.append(c_origin)
        li_origin[index], li_origin[d] = li_origin[d], li_origin[index]

if "".join(origin) != puzzle:
    print(-1)
