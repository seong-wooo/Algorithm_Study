def solution(arr):

    result = press(arr)
    return [result.count(0), result.count(1)]

    
def press(arr):
    if is_all_same(arr):
        return [arr[0][0]]
    
    l = len(arr)    
    arrs = [[] for _ in range(4)]
    for top in arr[:l//2]:
        arrs[0].append(top[:l//2])
        arrs[1].append(top[l//2:])
        
    for bottom in arr[l//2:]:
        arrs[2].append(bottom[:l//2])
        arrs[3].append(bottom[l//2:])
    
    result = []
    
    for a in arrs:
        result += press(a)
    
    return result
    
    

def is_all_same(arr):
    target = arr[0][0]    
    for j in range(len(arr)):
        for i in range(len(arr[0])):
            if arr[j][i] != target:
                return False
    return True
        
