# 이게 왜 이분탐색이지 ? 라는 고민을 되게 오래하였음
# 일정 범위 내에서 찾고자하는 수가 있다면 이분 탐색을 고려해보아야한다
# sum([x // mid for x in lan]) 이런 스킬도 배울 수 있었다.


from sys import stdin

k, n = map(int, stdin.readline().split())

lan = []

for i in range(k):
    lan.append(int(stdin.readline()))

low = 1
high = max(lan)

while low <= high:
    mid = (low+high)// 2
    count = sum([x // mid for x in lan])

    if count >= n:
        low = mid + 1

    else:
        high = mid - 1


print(high)

