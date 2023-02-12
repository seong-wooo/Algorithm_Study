import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

blocks = []
count = 0
max_blocks = 0
min_blocks = sys.maxsize
for i in range(n):
    blocks.append(list(map(int, input().split())))
    count += sum(blocks[-1])
    max_blocks = max(max_blocks, max(blocks[-1]))
    min_blocks = min(min_blocks, min(blocks[-1]))


# (최대 높이는 전체 블록 갯수 / 땅넓이) or (가장 높은 block 의 높이) 둘 중 작은 값
max_h = min((count + b) // (n * m), max_blocks)

min_times = 0
hh = min_blocks
for j in range(n):
    for i in range(m):
        if blocks[j][i] > min_blocks:
            min_times += (blocks[j][i] - min_blocks) * 2
        else:
            min_times += min_blocks - blocks[j][i]


for h in range(min_blocks + 1, max_h + 1):
    h_time = 0
    for j in range(n):
        for i in range(m):
            if blocks[j][i] > h:
                h_time += (blocks[j][i] - h) * 2
            else:
                h_time += h - blocks[j][i]

    if min_times < h_time:
        print(min_times, hh)
        exit(0)

    min_times = h_time
    hh = h

print(min_times, hh)