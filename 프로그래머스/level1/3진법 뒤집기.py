def solution(n):
    # 10진법 -> 3진법 만들기

    base3 = ""

    while n > 0:
        n, m = n // 3, n % 3
        base3 += str(m)

    # base3은 이미 뒤집힌 상태
    return int(base3, 3)