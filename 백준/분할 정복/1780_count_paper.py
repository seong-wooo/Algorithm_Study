# 각 종이를 문자열로 return 하여 더해주고
# 마지막에 나온 문자열에서 각 요소의 개수를 셌다.
# 분할 정복을 점점 정복해가는 느낌
# 2630,1992,1780 문제 전부 비슷한 방법으로 풀이했다.
# 글로벌 변수를 사용하는 방법도 존재한다.

import sys


def divide_paper(paper, x, y, N):
    if N == 1:
        if paper[x][y] == -1:
            return "-"
        return str(paper[x][y])

    color = paper[x][y]
    count = ""
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != color:
                for k in range(3):
                    for l in range(3):
                        count += divide_paper(paper, x+(N*k)//3, y+(N*l)//3, N//3)
                return count
    if color == -1:
        return "-"
    return str(color)



N = int(sys.stdin.readline())



paper =[]

for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))


s = divide_paper(paper,0,0,N)
print(s.count("-"))
print(s.count("0"))
print(s.count("1"))