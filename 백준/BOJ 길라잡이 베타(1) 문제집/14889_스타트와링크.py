# 조합을 사용하면 4개씩 나뉜 튜플의 집합으로 나타난다.
# 조합을 리스트로 만들면 0번째와 n-1번째가 세트가 되고 1번째와 n-2번째 ... 이런식으로 세트가 만들어진다.
# 각 세트에서 각각의 스탯을 구한 뒤 최소값을 구한다.
# 최솟값을 구할 때  처음에는 l_count ,r_count로 나눠서 for문을 2개 돌렸다
# 후에 count라는 변수 하나로 for문 1개로 바꿨더니 동작 시간이 줄어들었다.

from itertools import combinations

n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]

for j in range(n):
    for i in range(j):
        s[i][j] += s[j][i]

# j > i j랑 i 랑 팀이면 [j][i] 찾으면됨
zton = [i for i in range(n)]

div = list(combinations(zton, n // 2))
# 처음~절반  / 절반+1 ~ 마지막

min_stat = 999999999
for i in range(len(div) // 2):
    left = div[i]
    right = div[-1 - i]
    count = 0
    for i in range(n // 2):
        for j in range(i+1, n//2):
            count += s[left[i]][left[j]]
            count -= s[right[i]][right[j]]

    min_stat = min(min_stat, abs(count))

print(min_stat)