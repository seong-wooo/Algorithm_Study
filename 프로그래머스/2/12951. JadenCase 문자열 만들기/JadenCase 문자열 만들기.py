def solution(s):
    
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isalpha():
            if i == 0 or s[i-1] == " ":
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
                
    return "".join(s)
        
              
