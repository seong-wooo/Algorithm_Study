def solution(numbers):
    a =[1,2,3,4,5,6,7,8,9]
    result = 0
    for i in a:
        if i not in numbers:
            result+=i
    return result


# 여진수
def solution(numbers):
    return 45 - sum(numbers)