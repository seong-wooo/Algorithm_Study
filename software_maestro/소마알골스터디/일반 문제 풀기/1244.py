# 남 n -> 2n의 상태 바꿈
# 여 n -> 좌우가 대칭이면서 가장 많은 스위치 포함하는 구간 상태 변경

import sys

input = sys.stdin.readline

n = int(input())
switch = [-1] + list(map(int, input().split()))

students = int(input())

for i in range(students):
    성별, 번호 = map(int, input().split())

    if 성별 == 1:
        switch[번호::번호] = map(lambda x: 1 - x, switch[번호::번호])

    else:
        i = 1
        while 번호 + i < len(switch) and 번호 - i > 0 and switch[번호 + i] == switch[번호 - i]:
            i += 1

        switch[번호 - i + 1:번호 + i] = map(lambda x: 1 - x, switch[번호 - i + 1:번호 + i])

switch = switch[1:]
i = 0
while i < len(switch):
    print(*switch[i:i+20])
    i += 20


