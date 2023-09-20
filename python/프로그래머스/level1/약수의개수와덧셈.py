def solution(left, right):
    # 제곱근이 정수이면 홀수
    # 정수가 아니면 짝수
    result = 0
    for num in range(left, right +1):
        if (num**0.5)%1 == 0:
            result -= num
        else:
            result += num
    return result