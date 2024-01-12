import re

def solution(dartResult):
    result = [0] * 3
    bonus = {
        "S" : 1,
        "D" : 2,
        "T" : 3
    }
    
    option = {
        "*" : (2, 2),
        "#" : (1, -1)
    }
    dart = [r for r in re.split(r"(\d+\D+)", dartResult) if r]
    
    for i in range(len(dart)):
        j = 1
        while j < len(dart[i]) and dart[i][j].isdigit():
            j += 1
        
        num = int(dart[i][:j])

        if len(dart[i]) > j:
            num **= bonus[dart[i][j]]
            for k in range(j+1, len(dart[i])):
                b, c = option[dart[i][k]]
                num *= c
                if i > 0:
                    result[i-1] *= b
        
        result[i] = num
    return sum(result)
            