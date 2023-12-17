def solution(data, col, row_begin, row_end):

    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    result = 0
    for i in range(row_begin - 1, row_end):
        row = data[i]
        result ^= sum(map(lambda x: x % (i + 1), row))
    
    return result
        