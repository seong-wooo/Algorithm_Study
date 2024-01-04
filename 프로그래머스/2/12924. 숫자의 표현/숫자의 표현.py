def solution(n):
    nums = [ i * (i + 1) // 2 for i in range(n//2 + 2)]

    answer = 0
    for right in range(1, n//2 + 2):
        left = right - 1
        while left > 0 and nums[right] - nums[left] < n:
            left -= 1
            
        if nums[right] - nums[left] == n:
            answer += 1

    
    return answer + 1 if n > 2 else answer
            