# 경우의 수를 리스트로 나열하고
# 경우의 수를 만족하는 항목을 구한다.


def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    a = [0, 0, 0]

    # 1번 수포자
    for i in range(len(answers)):
        # 1번 수포자
        if answers[i] == a1[i % 5]:
            a[0] += 1
        # 2번 수포자
        if answers[i] == a2[i % 8]:
            a[1] += 1
        # 3번 수포자
        if answers[i] == a3[i % 10]:
            a[2] += 1

    max_a = max(a)
    b = []
    for i in range(3):
        if a[i] == max_a:
            b.append(i + 1)

    return b