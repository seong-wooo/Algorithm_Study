def solution(k, ranges):
    
    nums = [k]
    
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k *= 3
            k += 1
        nums.append(k)
    
    answer = []
    for a, b in ranges:
        b += len(nums) - 1    
        if a > b:
            answer.append(-1)
            continue

        result = 0
        for i in range(a, b):
            result += (nums[i] + nums[i+1]) / 2
        answer.append(result)
        
    return answer