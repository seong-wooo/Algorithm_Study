# 체육복을 줄 때 앞에 있는 사람 것을 먼저 가져오는 방법을 사용하였다.
# 앞에 있는 사람 것은 남는 것이지만
# 뒤에 있는 사람 것은 뒤뒤 사람의 것일수도 있으므로

# 나의 코드
from collections import Counter


def solution(n, lost, reserve):
    student = [-1] + [1 for _ in range(n)] + [-1]

    for i in lost:
        student[i] -= 1
    for i in reserve:
        student[i] += 1

    for i in range(1, len(student) - 1):
        if student[i] == 0:
            if student[i - 1] == 2:
                student[i - 1] = 1
                student[i] = 1

            elif student[i + 1] == 2:
                student[i + 1] = 1
                student[i] = 1

    return n - Counter(student)[0]

# 다른사람의 코드
# 나와는 다르게 조건을 만족하지 못하는 요소를 찾은 것이 아니라
# 조건을 만족하는 요소를 이용하여 시간을 더 절약하였다.

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
