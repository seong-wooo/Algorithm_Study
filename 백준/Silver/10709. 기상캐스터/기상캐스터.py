import sys

input = sys.stdin.readline
h, w = map(int, input().split())

clouds = [input().rstrip() for _ in range(h)]

answer = [["-1"] * w for _ in range(h)]

for j in range(h):
    time = -1
    for i in range(w):
        if time != -1 and clouds[j][i] == ".":
            answer[j][i] = str(time)
            time += 1

        elif clouds[j][i] == "c":
            answer[j][i] = "0"
            time = 1

for a in answer:
    print(" ".join(a))