def solution(num):

    result = 0
    while num != 1 and result <= 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1
        result += 1

    return result if result <= 500 else -1