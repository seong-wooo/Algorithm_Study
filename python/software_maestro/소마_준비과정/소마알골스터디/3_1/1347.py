import sys

input = sys.stdin.readline

n = int(input())

move = input().rstrip()

miro = [["#"] * 102 for i in range(102)]

# F 앞으로 한 칸 /  L, R 왼쪽 오른쪽으로 방향만 전환

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def F(direction, y, x):
    ny = y + dy[direction]
    nx = x + dx[direction]
    miro[ny][nx] = "."

    return ny, nx


direction = 0
y, x = 50, 50
miro[y][x] = "."
for i in range(len(move)):
    if move[i] == "F":
        y, x = F(direction, y, x)

    elif move[i] == "L":
        direction = direction - 1 if direction != 0 else 3

    else:
        direction = direction + 1 if direction != 3 else 0

result = []
dot_index = []
for m in miro:
    if "." in m:
        result.append(m)
        dot_index.append((m.index("."), m[::-1].index(".")))

start = min(dot_index, key=lambda x: x[0])[0]
end = 102 - min(dot_index, key=lambda x:x[1])[1]

for r in result:
    print("".join(r[start:end]))
