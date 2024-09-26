# A 덩어리를 찾는다.
# A 덩어리를 기준으로 빠꾸할지, 직진할지 결정한다.
# A 덩어리마다 계산을 해본다.

def solution(name):
    count = list(map(lambda x : min(ord(x) - ord('A'), ord('Z') - ord(x) + 1), list(name)))
    answer = sum(count)
    min_move = len(count) - 1
    print(count)
    i = 0
    while i < len(count):
        if count[i] == 0:
            j = i + 1
            while j < len(count) and count[j] == 0:
                j += 1
            
            # move 할 수 있는 경우는 총 3가지
            # 직진하기 / 앞으로 갔다가 뒤로 / 뒤로 갔다가 앞으로
            
            # 1. 직진하기
            move = i - 1 if i > 0 else 0
            move += min(move, len(count) - j)
            move += len(count) - j
            
            min_move = min(min_move, move)
            
            
            i = j - 1
        i += 1
        
    return answer + min_move