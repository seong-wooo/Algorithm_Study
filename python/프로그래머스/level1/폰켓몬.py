# 내가 푼 방법
def solution(nums):
    length = len(nums)

    if len(set(nums)) >= length//2:
        return length // 2
    else:
        return len(set(nums))

# 다른 방법
def solution(nums):
    return min(len(set(nums)), len(nums) // 2)