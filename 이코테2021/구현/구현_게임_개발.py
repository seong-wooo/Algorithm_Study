# 게임 개발

# 내가 푼 풀이

# 방향에 따라 갈 곳을 나눈다.

# 0: 북쪽 -> 열 - 1
# 1: 동쪽 -> 행 - 1
# 2: 남쪽 -> 열 + 1
# 3: 서쪽 -> 행 + 1
# 0 -> 3-> 2-> 1

# 마지막 조건을 안넣었다.. 내가 쓴 코드는 틀렸음 ...

# n, m = map(int, input().split())
# a, b, v = map(int, input().split())
# mapp = []
# for i in range(n):
#     mapp.append(list(map(int, input().split())))
#
# loc = [a, b]
# mapp[a][b] = 1
# count = 1
# while True:
#     if v == 0:
#         if mapp[loc[0]][loc[1] - 1] == 0 :
#             mapp[loc[0]][loc[1] - 1] = 2
#             loc[1] -= 1
#             count += 1
#         else:
#             v = 3
#
#     elif v == 1:
#         if mapp[loc[0] - 1][loc[1]] == 0:
#             mapp[loc[0] - 1][loc[1]] = 2
#             loc[0] -= 1
#             count += 1
#         else:
#             v = 0
#
#     elif v == 2:
#         if mapp[loc[0]][loc[1] + 1] == 0:
#             mapp[loc[0]][loc[1] + 1] = 2
#             loc[1] += 1
#             count += 1
#         else:
#             v = 1
#
#
#     else:
#         if mapp[loc[0] + 1][loc[1]] == 0:
#             mapp[loc[0] + 1][loc[1]] = 2
#             loc[0] += 1
#             count += 1
#         else:
#             v = 2
#
#     if mapp[loc[0] + 1][loc[1]] == 1 and mapp[loc[0] - 1][loc[1]] == 1 and mapp[loc[0]][loc[1] + 1] == 1 and mapp[loc[0]][loc[1] - 1] == 1:
#         break
# print(count)



#나는 경우의 수를 모두 구했다.
#책에서는 경우의 수를 dx,dy로 일반화하여 구하였다.


# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# 새로운 2차원 배열을 만드는 이유 -> 본래의 2차월 배열을 수정하지 않기위해
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기

x, y, direction = map(int, input().split())


d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))


# 북, 동, 남, 서 방향 정의
# 각 방향을 보고 있을 때 이동 거리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
# 글로벌 변수를 사용했다.
# 글로벌 변수의 사용법도 익히자
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1

# 4 바퀴 모두 돌았음을 알려주는 변수
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)