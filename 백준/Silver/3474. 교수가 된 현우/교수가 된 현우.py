import sys

input = sys.stdin.readline

answer =[]
for _ in range(int(input())):
    n = int(input())
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    answer.append(count)


print("\n".join(map(str, answer)))



