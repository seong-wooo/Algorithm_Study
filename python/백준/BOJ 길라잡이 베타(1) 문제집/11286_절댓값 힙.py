# 음수 값을 따로 모아서
# 만약 음수값이 존재한다면
# pop을 한 후 음수로 만들기
import sys
import heapq

n = int(sys.stdin.readline())
h = []
c = {}
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if h:
            y = heapq.heappop(h)
            if -y in c and c[-y] > 0:
                c[-y] -= 1
                print(-y)
            else:
                print(y)
        else:
            print("0")
    else:
        if x < 0:
            if x in c:
                c[x] += 1
            else:
                c[x] = 1
        heapq.heappush(h, abs(x))


