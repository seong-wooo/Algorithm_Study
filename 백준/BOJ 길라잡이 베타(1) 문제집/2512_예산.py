# 이분 탐색으로 풀지 않았다.
# 이분탐색으로 상한액을 찾아가는 방식으로도 풀 수 있다.
n,c,h = int(input()), list(map(int, input().split())), int(input())

c.sort()
result = 0
for i in range(len(c)):
    if c[i] * (n-i) <= h:
        h -= c[i]
    else:
        result = h // (n-i)
        break

print(result if result else c[-1])