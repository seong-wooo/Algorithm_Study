def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))] 
    
    for j in range(len(arr1)):
        for i in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[j][i] += arr1[j][k] * arr2[k][i]
    
    
    return answer


# 1 4     3 4 3
# 3 2     5 6 3
# 4 1