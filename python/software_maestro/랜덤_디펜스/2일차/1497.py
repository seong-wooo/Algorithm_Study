import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
g =[]

for _ in range(n):
    guitar, info = input().split()
    s = set()
    for i in range(m):
        if info[i] == "Y":
            s.add(i + 1)

    g.append((guitar, s))


def total():
    total = set()
    for guitar, s in g:
        total |= s

    return len(total)

total = total()

def result():
    for i in range(1, n + 1):
        for c in combinations(g, i):
            ss = set()
            for guitar, s in c:
                ss |= s

            if len(ss) == total:
                return i
    return -1

if total == 0:
    print("-1")
else:
    print(result())


# 삼성 SW 역량테스트 혹은 카카오 코딩 테스트 유형 문제
# 옛날에는 파이썬 itertools 쓸 수 있었는데 이제는 못 쓴다.
# 삼성전자 시험 준비하면 DFS로 아래 4개 외우듯이 짜야함
# 1. 순열
# 2. 중복순열
# 3. 조합
# 4. 중복 조합
