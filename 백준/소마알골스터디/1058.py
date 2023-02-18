import sys

input = sys.stdin.readline

n = int(input())
friends =[list(input().rstrip()) for i in range(n)]
e_friends = [[0] * n for _ in range(n)]

for j in range(n):
    for i in range(n):
        if friends[j][i] == "Y":
            e_friends[j][i] = 1
        else:
            if i != j:
                for k in range(n):
                    if friends[j][k] == friends[i][k] == "Y":
                        e_friends[i][j] = e_friends[j][i] = 1



max_friends = 0
for i in range(n):
    max_friends = max(max_friends, sum(e_friends[i]))

print(max_friends)