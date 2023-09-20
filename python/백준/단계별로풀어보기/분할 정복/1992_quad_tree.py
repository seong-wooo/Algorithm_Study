# 2630과 비슷한 문제
# 괄호의 위치를 넣는 것이 어려웠음
# 2차원 배열을 4분할 하여 각각의 리턴값을 더해주었음

import sys


def quad_tree(tree, x, y, N):
    if N == 1:
        return str(tree[x][y])

    bit = tree[x][y]
    press=""
    for i in range(x, x+N):
        for j in range(y,y+N):
            if tree[i][j] != bit:
                press += "("
                press += quad_tree(tree, x, y, N//2)
                press += quad_tree(tree, x, y+N//2, N//2)
                press += quad_tree(tree, x+N//2, y, N//2)
                press += quad_tree(tree, x+N//2, y+N//2, N//2)
                press +=")"
                return press
    return bit

N = int(sys.stdin.readline())
tree=[]
for i in range(N):
    tree.append(sys.stdin.readline().strip())
print(quad_tree(tree,0,0,N))