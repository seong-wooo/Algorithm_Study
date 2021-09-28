# 상하좌우
# 2차원 배열에서 현재 위치의 인덱스를 i,j 라고 한다.
# L: j!=0일 때 R: j!=n-1 일 때 U: i!=0일 때 D: i!=n-1일 때 이동

# 내가 쓴 풀이의 문제점: 지금 문제에서는 4가지 경우에 대해서만 조건식을 세우기 때문에
# 4가지를 모두 나열하면 되지만
# 경우의 수가 더 많을 경우에는 일반화를 해야한다.

import sys

n = int(sys.stdin.readline())

command = list(sys.stdin.readline().split())

loc = [0, 0]
for c in command:
    if c == 'L' and loc[0] > 0:
        loc[0] -= 1
    elif c == 'R' and loc[0] < n - 1:
        loc[0] += 1
    elif c == 'U' and loc[1] > 0:
        loc[1] -= 1
    elif c == 'D' and loc[1] < n - 1:
        loc[1] += 1

print(loc[1] + 1, loc[0] + 1)

#############################

# 위 코드보다 일반화를 하여 나타낸 코드

n = int(input())
x, y = 1, 1
plans = input().split()


# LRUD에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    # 범위 안에 존재하는지 확인
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동
    x, y = nx, ny

print(x, y)