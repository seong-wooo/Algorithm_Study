import sys

friends = []

for i in range(int(sys.stdin.readline())):
    x, y, w, h = map(int, sys.stdin.readline().split())
    friends.append([[x-w,x+w], [y-h, y+h]])


result = friends[0]

for i in range(1, len(friends)):
    result[0][0] = max(result[0][0], friends[i][0][0])
    result[0][1] = min(result[0][1], friends[i][0][1])
    result[1][0] = max(result[1][0], friends[i][1][0])
    result[1][1] = min(result[1][1], friends[i][1][1])

if result[0][0] > result[0][1] or result[1][0] > result[1][1]:
    print("impossible")
else:
    print(result[0][0], result[1][0])

