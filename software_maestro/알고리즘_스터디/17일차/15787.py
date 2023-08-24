import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trains = [[0]* 20 for _ in range(n)]

history = set()

for _ in range(m):
    commands = list(map(int, input().split()))

    if commands[0] == 1:
        i = commands[1] - 1
        x = commands[2] - 1

        trains[i][x] = 1

    elif commands[0] == 2:
        i = commands[1] - 1
        x = commands[2] - 1

        trains[i][x] = 0

    elif commands[0] == 3:
        i = commands[1] - 1

        trains[i] = [0] + trains[i][:-1]

    else:
        i = commands[1] - 1

        trains[i] = trains[i][1:] + [0]


result = 0
for train in trains:
    train = "".join(map(str, train))
    if train not in history:
        history.add(train)
        result += 1

print(result)