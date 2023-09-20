import sys

input = sys.stdin.readline

n = int(input())

line = [int(input()) for _ in range(n)]


s_line = set(line)

result = 1
for x in s_line:

    ex_x = 1

    for i in range(len(line) - 1):
        if line[i] != x:
            for j in range(i + 1, len(line)):
                if line[j] != x:
                    if line[i] == line[j]:
                        ex_x += 1
                        result = max(result, ex_x)
                    else:
                        ex_x = 1
                    break

print(result)