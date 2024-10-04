import re

def solution(n, k):
    s = ntok(n,k)
    
    nums = [int(num) for num in re.split("0+",s) if num]

    
    return len([num for num in nums if num >= 2 and is_prime(num)])
    

def ntok(n, k):
    result = ""
    
    while n > 0:
        n, r = n//k, n%k        

        result = str(r) + result
    
    return result

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True