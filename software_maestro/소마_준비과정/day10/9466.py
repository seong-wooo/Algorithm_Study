import sys


def f(select, visited, i):
    expected_team = [i]
    visited[i] = True
    while not visited[select[i]]:
        visited[select[i]] = True
        expected_team.append(select[i])
        i = select[i]

    target = select[i]
    if target in expected_team:
        return expected_team.index(target)
    return len(expected_team)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    select = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n + 1)

    result = 0
    for i in range(1, n + 1):
        if not visited[i]:
            result += f(select, visited, i)

    print(result)

