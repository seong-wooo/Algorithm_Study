def solution(data, col, row_begin, row_end):
    
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    answer = sum(j % row_begin for j in data[row_begin - 1])
    
    for i in range(row_begin, row_end):
        answer ^= sum(j % (i+1) for j in data[i])
    return answer
        
    
