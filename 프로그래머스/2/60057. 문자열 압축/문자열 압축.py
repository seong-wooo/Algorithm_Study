def solution(s):
    answer = len(s)
    for cut in range(1, len(s)//2 + 1):
        result = ""
        i = 0
        while i < len(s):
            j = i + cut
            count = 1
            while j < len(s) and s[i:i+cut] == s[j:j+cut]:
                j += cut
                count += 1
            

            result += str(count) + s[i:i+cut] if count > 1 else s[i:i+cut]        
            i = j
            

        
        answer = min(answer, len(result))
    return answer
            
        
        
        