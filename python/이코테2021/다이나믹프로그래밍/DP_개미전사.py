# 개미 전사
# i번째 식량을 가져간다고 할 때
# i-2 , i-3 번째에서 i 번째로 넘어오는 두 경우를 생각하여
# 두 경우를 비교하여 큰 값을 선택했다.

n = int(input())
array = list(map(int, input().split()))
dp = [array[0], array[1], array[0] + array[2]] + (n - 3) * [0]


for i in range(3, len(array)):
    dp[i] = max(dp[i - 2], dp[i - 1]) + array[i]

print(max(dp[-1], dp[-2]))

# 다른 방법
# i번째까지 도달했을 때 얼마만큼의 식량을 가져갈 수 있느냐

n = int(input())
array = list(map(int, input().split()))
dp = [array[0], max(array[0],array[1])] + (n - 2) * [0]

for i in range(3, len(array)):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(max(dp[-1], dp[-2]))
