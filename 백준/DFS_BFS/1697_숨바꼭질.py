# 1행에 대해서 bfs 반복
# visited 를 visited = [0] * (k+1)로 살행했을 때 틀렸다고 나왔다.
# 왜인지 궁금하다..
# k로 범위를 정해놓고 0 <=nx[i] < k+1 로 nx[i] 범위를 제한하면 되는 것 아닌가..

# 자세히 생각해보니 x가 k의 값을 벗어날 수도 있다.
# (k+2) -1 -1 같은 경우가 있을 수 있으므로
# 범위를 크게 해줘야한다. 차라리 2*k로 했으면 맞았을 수도

# 2*k + 1로 하면 시간이 두배로 걸렸다.
# 2*k + 1의 연산을 계속 해줘야 하기 때문인 것 같다.
# * 그냥 상수 최대 범위 떄려넣기 *

from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n - k)
    exit()

visited = [0] * 100001

queue = deque()
queue.append(n)

visited[n] = 1

while queue:
    x = queue.popleft()
    nx = [x - 1, x + 1, 2 * x]

    for i in range(3):
        if 0 <= nx[i] < 100001 and visited[nx[i]] == 0:
            visited[nx[i]] = visited[x] + 1
            if nx[i] == k:
                print(visited[k] - 1)
                break
            queue.append(nx[i])