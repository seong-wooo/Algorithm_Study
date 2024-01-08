import math

def solution(s):
    answer = len(s)
    
    for length in range(1, len(s) // 2 + 1):
        
        i = 0
        result = len(s)
        while i <= len(s) - length * 2:
            press = 0
            while i <= len(s) - length * 2 and s[i:i+length] == s[i+length:i+2*length]:
                i += length
                press += 1
            
            if press:
                result -= press * length - len(str(press + 1))
                
            else:
                i += length
            

        answer = min(answer, result)
    
    return answer
            