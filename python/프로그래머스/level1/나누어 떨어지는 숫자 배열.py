def solution(arr, divisor):
    result = sorted([x for x in arr if x % divisor == 0])
    return result if result else [-1]