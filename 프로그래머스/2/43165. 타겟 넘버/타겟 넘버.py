import sys

def solution(numbers, target):
    sys.setrecursionlimit(10**6)
    
    return answer(numbers, target, 0, 0)


def answer(numbers, target, index, current):
    if index == len(numbers):
        return 1 if target == current else 0
    
    return answer(numbers, target, index + 1, current + numbers[index]) + answer(numbers, target, index + 1, current - numbers[index])