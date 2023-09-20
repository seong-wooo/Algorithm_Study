# 분할 정복을 리스트를 이용하여서 구하였다.
# 리스트를 안쓰고 다시 구현해봐야겠다.

import sys

def div_N(p):
    if len(p) == 1:
        if p[0][0] == 1:
            return "b"
        else:
            return "w"

    N = len(p)
    color = ""
    paper = p[0][0]
    for i in range(N):
        for j in range(N):
            if p[i][j] != paper:
                p1 =[]
                p2 =[]
                p3 =[]
                p4 =[]
                for k in range(N // 2):
                    p1.append(p[k][:N // 2])
                    p2.append(p[k][N // 2:])
                    p3.append(p[k + N // 2][:N // 2])
                    p4.append(p[k + N // 2][N // 2:])
                color += div_N(p1)
                color += div_N(p2)
                color += div_N(p3)
                color += div_N(p4)
                return color
    if paper == 1:
        return "b"
    else:
        return "w"



N = int(sys.stdin.readline())
p = []

for i in range(N):
    p.append(list(map(int, sys.stdin.readline().split())))

s = div_N(p)
print(s.count("w"))
print(s.count("b"))


######################################################
# 리스트를 사용하지않고
# 범위만을 이용하여 분할 정복을 구현하였다.


# import sys
#
# def div_N(p,x, y, N):
#     color = ""
#     paper = p[x][y]
#
#     for i in range(x, x+N):
#         for j in range(y, y+N):
#             if paper != p[i][j]:
#                 color += div_N(p, x, y, N//2)
#                 color += div_N(p, x, y+N//2, N//2)
#                 color += div_N(p, x+N//2, y, N//2)
#                 color += div_N(p, x+N//2, y+N//2, N//2)
#                 return color
#
#     if paper == 1:
#         return "b"
#     else:
#         return "w"
#
#
#
#
#
# N = int(sys.stdin.readline())
# p = []
#
# for i in range(N):
#     p.append(list(map(int, sys.stdin.readline().split())))
#
# s = div_N(p,0,0,N)
# print(s.count("w"))
# print(s.count("b"))