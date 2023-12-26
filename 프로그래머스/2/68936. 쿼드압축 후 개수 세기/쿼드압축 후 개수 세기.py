def solution(arr):

    answer = [0, 0]
    
    def is_all_same(arr, y, x, l):
        target = arr[y][x]    
        for j in range(y, y + l):
            for i in range(x, x + l):
                if arr[j][i] != target:
                    return False
        return True
    
    
    def press(arr, y, x, l):
        if is_all_same(arr, y, x, l):
            answer[arr[y][x]] += 1
            return
        
        
        press(arr, y, x, l // 2)
        press(arr, y + l // 2, x, l // 2)
        press(arr, y, x + l // 2, l // 2)
        press(arr, y + l // 2, x + l // 2, l // 2)
        
    
    press(arr, 0, 0, len(arr))
    
    return answer