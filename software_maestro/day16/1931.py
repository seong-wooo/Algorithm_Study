import sys

input = sys.stdin.readline

lec = [list(map(int, input().split())) for _ in range(int(input()))]

lec.sort(key=lambda x: (x[1], x[0]))

cur_time = lec[0][1]
result = 1
for i in range(1, len(lec)):
    if lec[i][0] >= cur_time:
        cur_time = lec[i][1]
        result += 1

print(result)