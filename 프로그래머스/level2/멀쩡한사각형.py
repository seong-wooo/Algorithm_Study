# 사각형을 자를 때 w, h가 서로소일 때 
# 가로로 w만큼 이동함 -> 이동 과정 중 w-1개 잘림 
# 세로로는 h만큼 이동함


from math import gcd
def solution(w,h):
    # 가로로 옮기는 횟수 w-1
    # 세로 개수 h
    g = gcd(w,h)
    w_g, h_g = w//g, h//g

    # w_g , h_g 블록에서 잘리는 사각형
    cut = w_g-1 + h_g


    return w*h - (cut * g)
