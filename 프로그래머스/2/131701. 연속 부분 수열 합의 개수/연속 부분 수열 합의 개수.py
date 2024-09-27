def solution(elements):
    answer = set(elements)
    
    i = 0 
    
    while i < len(elements):
        current = elements[i]
        answer.add(current)
        j = (i + 1) % len(elements)
        
        while j != i:
            current += elements[j]
            answer.add(current)
            j += 1
            j %= len(elements)
        i += 1
    return len(answer)