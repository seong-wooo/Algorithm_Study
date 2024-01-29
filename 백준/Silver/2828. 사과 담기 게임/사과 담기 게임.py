import sys
input = sys.stdin.readline

n, m = map(int, input().split())
apples = [int(input()) for _ in range(int(input()))]

loc = 0
answer = 0
for apple in apples:
    if apple > loc + m:
        move = apple - m - loc
        loc += move
        answer += move
    elif apple <= loc:
        move = loc - apple + 1
        loc -= move
        answer += move

print(answer)

