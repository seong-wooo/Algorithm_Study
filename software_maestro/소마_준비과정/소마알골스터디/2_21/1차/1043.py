import sys
input = sys.stdin.readline

n, m = map(int, input().split())

t_n, *true_mans = map(int, input().split())

true_mans = set(true_mans)
party = [{} for _ in range(m)]

for i in range(m):
    p_n, *p_nums = map(int, input().split())
    p_nums = set(p_nums)
    party[i] = p_nums


for j in range(m):
    for i in range(m):
        if true_mans & party[i]:
            true_mans |= party[i]

count = 0
for i in range(m):
    if not (true_mans & party[i]):
        count += 1

print(count)

