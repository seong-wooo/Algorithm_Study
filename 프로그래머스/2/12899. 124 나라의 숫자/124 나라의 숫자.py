def solution(n):
    answer = ''
    nums = ["4", "1", "2"]
    
    while n >= 1:
        c = n % 3
        answer = nums[c] + answer
        n -= c if c != 0 else 3
        n //= 3
        
    
    return answer
