import sys
def solution(line):
    dots = set()
    
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            a = line[i]
            b = line[j]
            if (a[0]*b[1] != a[1]*b[0]):
                x = (a[1]*b[2] - a[2]*b[1]) / (a[0]*b[1] - a[1]*b[0])
                y = (a[0]*b[2] - a[2]*b[0]) / (a[1]*b[0] - a[0]*b[1])
                
                if (x % 1 == 0 and y % 1 == 0):
                    dots.add(( int(y), int(x)))
    
    
    left = sys.maxsize
    right = -sys.maxsize    
    top = sys.maxsize    
    bottom = -sys.maxsize    
    
    for dot in dots:
        left = min(left, dot[1])
        right = max(right, dot[1])        
        top = min(top, dot[0])        
        bottom = max(bottom, dot[0])  
        
    answer = ["."*(right - left + 1) for _ in range(bottom - top + 1)]
    
    for dot in dots:
        y = dot[0]
        x = dot[1]
        
        l = list(answer[bottom - y])
        l[x - left] = "*"
        answer[bottom - y] = "".join(l)
        
        
        
    return answer