# 모든 숫자를 대상으로 + 로 계산했을 경우, -로 계산했을 경우를 구한다.
# 되게 간단하게 풀었던 문제이다.


def dfs(array, target, result):
    if len(array) == 1:
        if target == result + array[0] or target == result - array[0]:
            return 1
        else:
            return 0
    count = 0
    count += dfs(array[1:], target, result + array[0])
    count += dfs(array[1:], target, result - array[0])
    return count

def solution(numbers, target):
    return dfs(numbers, target,0)