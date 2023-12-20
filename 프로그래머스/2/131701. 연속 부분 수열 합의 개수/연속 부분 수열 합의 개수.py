def solution(elements):
    for i in range(1, len(elements)):
        elements[i] += elements[i - 1]
    
    elements = [0] + elements
    
    answer = set()
    
    for left in range(len(elements) - 1):
        for right in range(left + 1, len(elements)):
            total = elements[right] - elements[left]
            answer.add(total)
            answer.add(elements[-1] - total)
    
    return len(answer) - 1