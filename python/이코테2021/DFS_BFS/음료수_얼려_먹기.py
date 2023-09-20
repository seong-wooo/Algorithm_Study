# 음료수 얼려먹기
# bfs를 이용한다
# 방문한 곳은 1으로 바꾸기
import time
from collections import deque
import sys
import copy

#나는 bfs로 해결하였는데 dfs로 해결하였을 때 보다 bfs로 해결했을 때 더 빨랐다.
#대신 dfs로 해결했을 때 더 간결하게 코드를 작성할 수 있었다.

# bfs로 해결하기
def bfs(ice, row, col):
    ice_queue = deque()
    ice_queue.append((row, col))
    while ice_queue:
        row_, col_ = ice_queue.popleft()
        ice[row_][col_] = 1
        if row_ < len(ice) - 1 and ice[row_ + 1][col_] == 0 and (row_ + 1, col_) not in ice_queue:
            ice_queue.append((row_ + 1, col_))
        if row_ > 0 and ice[row_ - 1][col_] == 0 and (row_ - 1, col_) not in ice_queue:
            ice_queue.append((row_ - 1, col_))
        if col_ < len(ice[row_]) - 1 and ice[row_][col_ + 1] == 0 and (row_, col_ + 1) not in ice_queue:
            ice_queue.append((row_, col_ + 1))
        if col_ > 0 and ice[row_][col_ - 1] == 0 and (row_, col_ - 1) not in ice_queue:
            ice_queue.append((row_, col_ - 1))


# dfs로 해결하기
def dfs(ice, x, y):
    # 주어진 범위 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if ice[x][y] == 0:
        ice[x][y] = 1

        dfs(ice, x - 1, y)
        dfs(ice, x + 1, y)
        dfs(ice, x, y - 1)
        dfs(ice, x, y + 1)
        return True
    return False


n, m = map(int, sys.stdin.readline().split())

ice_list1 = []
for i in range(n):
    ice_list1.append(list(map(int, sys.stdin.readline().strip())))

ice_list2 = copy.deepcopy(ice_list1)

start_time1 = time.time()  # 측정 시작
# bfs 시작
result1 = 0
for i in range(n):
    for j in range(m):
        if ice_list1[i][j] == 0:
            bfs(ice_list1, i, j)
            result1 += 1
print(result1)

# 프로그램 소스코드
end_time1 = time.time()  # 측정 종료
print("bfs time:", end_time1 - start_time1)  # 수행 시간 출력

start_time2 = time.time()  # 측정 시작
# dfs 시작
result2 = 0
for i in range(n):
    for j in range(m):
        if dfs(ice_list2, i, j) == True:
            result2 += 1
print(result2)
# 프로그램 소스코드
end_time2 = time.time()  # 측정 종료
print("dfs time:", end_time2 - start_time2)  # 수행 시간 출력




