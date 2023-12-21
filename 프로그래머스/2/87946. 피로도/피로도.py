from itertools import permutations

def solution(k, dungeons):
    
    answer = 0
    for dungeon in permutations(dungeons, len(dungeons)):
        answer = max(answer, dfs(k, dungeon, 0))
    
    return answer
            

        

    
def dfs(k, dungeons, index):
    if k == 0 or index >= len(dungeons):
        return 0
    
    answer = dfs(k, dungeons, index + 1)
    
    if k >= dungeons[index][0]:
        answer = max(answer, 1 + dfs(k - dungeons[index][1], dungeons, index + 1))
    
    return answer
        
    