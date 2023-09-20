import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, w = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 리프 노드의 갯수

visited = [False] * (n + 1)


def isLeafNode(node):
    for next_node in graph[node]:
        if not visited[next_node]:
            return False

    return True


def dfs(node):
    if isLeafNode(node):
        return 1

    result = 0
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            result += dfs(next_node)
    return result

visited[1] = True
print(w / dfs(1))


# 모든 그래프 문제는 queue를 이용하는 것이 좋음