import sys

input = sys.stdin.readline

n = int(input())
hs = list(map(int, input().split()))

total = sum(hs)
if total % 3 != 0:
    print("NO")

else:
    x = total // 3

    # 2를 쓰는 횟수 = 1을 쓰는 횟수
    # 2를 x번 쓰고 1을 x번 쓸 수 있는 경우 -> YES

    count_two = 0
    for h in hs:
        count_two += h // 2

    if count_two < x:
        print("NO")

    else:
        print("YES")


# 코테 출제 빈도가 낮음: 골드 이상의 그리디, 다이나믹 프로그래밍 -> 뇌지컬을 요구하기 때문에
# 보통 코테 문제는 정형화 되어 있는 유형들을 충분히 연습했다면, 풀 수 있어야 된다.
# 이 문제는 그리디 유형: 문제 풀기위한 핵심 아이디어를 떠올려야함
# 먼저 점화식이나 해법을 떠올리고 그것이 맞는지 검증하는 방법
# 아이디어를 떠올린 뒤에 반박 가능한가? 를 판단해보기
