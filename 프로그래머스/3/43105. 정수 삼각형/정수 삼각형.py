def solution(triangle):
    
    dx = [-1, 0]
    
    for j in range(1, len(triangle)):
        for i in range(len(triangle[j])):
            max_route = 0
            for k in range(2):
                if 0 <= i + dx[k] < j:
                    max_route = max(max_route, triangle[j-1][i+dx[k]])
            triangle[j][i] += max_route
            
    return max(triangle[-1])