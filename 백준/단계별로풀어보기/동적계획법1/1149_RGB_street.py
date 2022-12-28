# 매 단계마다 정보를 저장한다
# 저장된 정보를 이용하여 다음 단계에서 활용한다.
# dynamic programing

import sys

n = int(sys.stdin.readline())
rgb = []
d = {}
for i in range(n):
    rgb.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])
print(min(rgb[-1]))