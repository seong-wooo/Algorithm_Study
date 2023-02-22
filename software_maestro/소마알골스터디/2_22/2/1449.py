import sys
input = sys.stdin.readline
# l칸까지 커버 가능
n, l = map(int, input().split())

w = [0] * 1001
for i in map(int, input().split()):
    w[i] = 1

w_count = 0
i = 1
while i <= 1000:
    if w[i] == 1:
        w_count += 1
        i += l
    else:
        i += 1

print(w_count)