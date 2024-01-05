import math

def solution(n, k):
    nums =[i for i in range(1, n + 1)]
    answer = []
    fact = math.factorial(len(nums) - 1)
    

    while nums:
        next_index = math.ceil(k / fact) - 1
        answer.append(nums.pop(next_index))
        k -= fact * next_index
        fact //= max(1, len(nums))
    
    return answer

    # k  f  nums     n_i
    # 5  2  [1,2,3]   
    
        
        