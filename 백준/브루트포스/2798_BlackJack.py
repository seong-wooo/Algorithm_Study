# 모든 경우의 수를 다 찾아봐야하는 브루트포스 문제
# 3개의 카드를 찾기위해 3중 for문을 이용하였다.
# 크게 어렵지 않았던 문제
n, m = map(int, input().split())

card = list(map(int, input().split()))

card3 = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1,n):
            result = card[i] + card[j] + card[k]
            if result <= m and result > card3:
                card3 = result

print(card3)
