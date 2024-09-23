def solution(progresses, speeds):
    index = 0
    answer = []
    
    while index < len(progresses):
        for i in range(index, len(progresses)):
            progresses[i] += speeds[i]
        
        new_index = index
        while new_index < len(progresses) and progresses[new_index] >= 100:
            new_index += 1
         

        if new_index != index:
            answer.append(new_index - index)
        index = new_index
        
    return answer