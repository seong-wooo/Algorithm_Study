def solution(n):
    return dfs([], n)
    
    
def dfs(arr, n):
    answer = 0
    
    if len(arr) == n:
        return 1
    
    s = set(range(n))
    row = len(arr)
    
    for i in range(row):
        s.discard(arr[i])
        s.discard(arr[i] - row + i)
        s.discard(arr[i] + row - i)
    
    
    for location in s:
        arr.append(location)
        answer += dfs(arr, n)
        arr.pop()
        
    return answer
    
        